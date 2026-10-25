import hashlib
from functools import lru_cache
from typing import Tuple

@lru_cache(maxsize=1024)
def compute_merkle_root(transactions: Tuple[str, ...]) -> str:
    if not transactions:
        return hashlib.sha256(b'').hexdigest()
    
    nodes = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]
    
    while len(nodes) > 1:
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])
        
        new_level = []
        for i in range(0, len(nodes), 2):
            combined = (nodes[i] + nodes[i+1]).encode()
            new_level.append(hashlib.sha256(combined).hexdigest())
        nodes = new_level
        
    return nodes[0]

def batch_process_signatures(signatures: list[str]) -> list[str]:
    return [hashlib.sha256(sig.encode()).hexdigest() for sig in signatures]

class CacheProvider:
    def __init__(self, size: int = 2048):
        self._cache = {}
        self._size = size

    def get_cached_hash(self, data: str) -> str:
        if data not in self._cache:
            if len(self._cache) >= self._size:
                self._cache.pop(next(iter(self._cache)))
            self._cache[data] = hashlib.sha256(data.encode()).hexdigest()
        return self._cache[data]