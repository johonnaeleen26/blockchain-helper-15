import hashlib
from functools import lru_cache
from typing import List, Sequence


@lru_cache(maxsize=2048)
def _double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


@lru_cache(maxsize=4096)
def combine_hashes(left: bytes, right: bytes) -> bytes:
    return _double_sha256(left + right)


class FastMerkleTree:
    def __init__(self, tx_hashes: Sequence[bytes]) -> None:
        self._leaf_hashes = list(tx_hashes)

    def get_root(self) -> bytes:
        if not self._leaf_hashes:
            return b"\x00" * 32

        current = self._leaf_hashes
        while len(current) > 1:
            if len(current) % 2 == 1:
                current.append(current[-1])

            next_level: List[bytes] = []
            for i in range(0, len(current), 2):
                next_level.append(combine_hashes(current[i], current[i + 1]))
            current = next_level

        return current[0]


def calculate_block_merkle_root(transactions: List[bytes]) -> str:
    leaf_hashes = [_double_sha256(tx) for tx in transactions]
    tree = FastMerkleTree(leaf_hashes)
    return tree.get_root().hex()
