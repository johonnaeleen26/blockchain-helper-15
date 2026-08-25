import hashlib
from typing import List

def calculate_hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def double_sha256(data: str) -> str:
    first = calculate_hash(data)
    return calculate_hash(first)

def validate_hex_string(hex_str: str) -> bool:
    if not hex_str:
        return False
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    try:
        int(hex_str, 16)
        return True
    except ValueError:
        return False

def validate_address(address: str) -> bool:
    if not address or not address.startswith('0x'):
        return False
    if len(address) != 42:
        return False
    return validate_hex_string(address[2:])

def wei_to_ether(wei_amount: int) -> float:
    if wei_amount < 0:
        raise ValueError("Amount cannot be negative")
    return wei_amount / 10 ** 18

def ether_to_wei(ether_amount: float) -> int:
    if ether_amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(ether_amount * 10 ** 18)

def create_transaction_hash(sender: str, receiver: str, amount: float, timestamp: int) -> str:
    data = f"{sender}{receiver}{amount}{timestamp}"
    return double_sha256(data)

def compute_merkle_root(transactions: List[str]) -> str:
    if not transactions:
        return calculate_hash("")
    hashes = [calculate_hash(tx) for tx in transactions]
    while len(hashes) > 1:
        new_hashes = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i + 1] if i + 1 < len(hashes) else left
            new_hashes.append(calculate_hash(left + right))
        hashes = new_hashes
    return hashes[0]