import functools
import hashlib
from typing import Any, Dict, List

class BlockProcessor:
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size

    @functools.lru_cache(maxsize=1024)
    def derive_hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def batch_process(self, transactions: List[Dict[str, Any]]) -> List[str]:
        return [self.derive_hash(str(tx)) for tx in transactions]

    @staticmethod
    def validate_integrity(hashes: List[str]) -> bool:
        return len(hashes) == len(set(hashes))

class TransactionManager:
    __slots__ = ('processor', 'buffer')

    def __init__(self):
        self.processor = BlockProcessor()
        self.buffer = []

    def append(self, tx: Dict[str, Any]) -> None:
        self.buffer.append(tx)

    def commit(self) -> List[str]:
        result = self.processor.batch_process(self.buffer)
        self.buffer.clear()
        return result