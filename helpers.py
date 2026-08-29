import hashlib
import re
from typing import Any, Dict

def wei_to_ether(wei: int) -> float:
    return wei / 10 ** 18

def ether_to_wei(ether: float) -> int:
    return int(ether * 10 ** 18)

def gwei_to_wei(gwei: float) -> int:
    return int(gwei * 10 ** 9)

def wei_to_gwei(wei: int) -> float:
    return wei / 10 ** 9

def encode_hex(data: bytes) -> str:
    return "0x" + data.hex()

def decode_hex(hex_string: str) -> bytes:
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    return bytes.fromhex(hex_string)

def keccak(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

def is_hex_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    if address.startswith("0x"):
        address = address[2:]
    if len(address) != 40:
        return False
    return bool(re.match(r"^[0-9a-fA-F]{40}$", address))

def normalize_address(address: str) -> str:
    address = address.lower()
    if not address.startswith("0x"):
        address = "0x" + address
    return address

def calculate_tx_hash(tx_data: Dict[str, Any]) -> str:
    data_str = str(sorted(tx_data.items()))
    hash_bytes = hashlib.sha256(data_str.encode()).digest()
    return encode_hex(hash_bytes)

def pad_left(data: bytes, length: int) -> bytes:
    if len(data) >= length:
        return data
    return b"\x00" * (length - len(data)) + data

def int_to_bytes(value: int, length: int = 32) -> bytes:
    return value.to_bytes(length, byteorder="big")

def bytes_to_int(data: bytes) -> int:
    return int.from_bytes(data, byteorder="big")

def validate_amount(amount: float) -> bool:
    return amount > 0