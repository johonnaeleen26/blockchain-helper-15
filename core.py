import functools
from typing import Callable, Any, Dict

CACHE_LIMIT = 1024

def memoize_blockchain_data(func: Callable) -> Callable:
    """Thread-safe lru cache for network-heavy calls."""
    @functools.lru_cache(maxsize=CACHE_LIMIT)
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper

class BatchProcessor:
    def __init__(self, items: list):
        self.items = items

    def process_generator(self):
        for item in self.items:
            yield self._transform(item)

    @staticmethod
    def _transform(item: Dict) -> Dict:
        return {k: v for k, v in item.items() if v is not None}

def compute_hash_sequence(data: bytes, iterations: int = 1000) -> bytes:
    import hashlib
    result = data
    for _ in range(iterations):
        result = hashlib.sha256(result).digest()
    return result

def optimized_filter(data_list: list, target_key: str) -> list:
    """List comprehension for high performance filtering."""
    return [item[target_key] for item in data_list if target_key in item]