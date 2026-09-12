import hashlib
from typing import List


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def calculate_merkle_root(tx_hashes: List[str]) -> str:
    if not tx_hashes:
        raise ValueError("transaction list cannot be empty")

    layer = [bytes.fromhex(tx.replace("0x", "")) for tx in tx_hashes]

    while len(layer) > 1:
        next_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i + 1] if i + 1 < len(layer) else left
            parent_hash = double_sha256(left + right)
            next_layer.append(parent_hash)
        layer = next_layer

    return layer[0].hex()


def validate_merkle_proof(
    tx_hash: str, proof: List[str], index: int, root: str
) -> bool:
    current_hash = bytes.fromhex(tx_hash.replace("0x", ""))
    for sibling_hex in proof:
        sibling = bytes.fromhex(sibling_hex.replace("0x", ""))
        if index % 2 == 0:
            current_hash = double_sha256(current_hash + sibling)
        else:
            current_hash = double_sha256(sibling + current_hash)
        index //= 2
    return current_hash.hex() == root.replace("0x", "")
