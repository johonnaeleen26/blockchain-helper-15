import hashlib
from functools import lru_cache
from typing import List


class BlockchainCore:
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size

    @staticmethod
    @lru_cache(maxsize=4096)
    def double_sha256(data: bytes) -> bytes:
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    def compute_merkle_root(self, tx_hashes: List[bytes]) -> bytes:
        if not tx_hashes:
            return b''

        current_level = tx_hashes
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                combined = left + right
                next_level.append(self.double_sha256(combined))
            current_level = next_level

        return current_level[0]

    @lru_cache(maxsize=1024)
    def verify_proof_of_work(self, header_hash: bytes, difficulty_target: int) -> bool:
        hash_int = int.from_bytes(header_hash, byteorder='big')
        return hash_int < difficulty_target
