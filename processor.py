import hashlib
from functools import lru_cache
from typing import List, Dict

class BlockProcessor:
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size

    @lru_cache(maxsize=1024)
    def derive_hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def batch_process(self, transactions: List[Dict]) -> List[str]:
        results = []
        for tx in transactions:
            payload = f"{tx['sender']}{tx['receiver']}{tx['amount']}"
            results.append(self.derive_hash(payload))
        return results

    def process_stream(self, stream: List[str]) -> List[str]:
        return [self.derive_hash(s) for s in stream]

    def clear_cache(self):
        self.derive_hash.cache_clear()