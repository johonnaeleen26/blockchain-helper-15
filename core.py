import functools
from typing import Callable, Any
from collections import deque

class CacheManager:
    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            if key in self.cache:
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            
            result = func(*args, **kwargs)
            
            if len(self.cache) >= self.capacity:
                oldest = self.order.popleft()
                del self.cache[oldest]
            
            self.cache[key] = result
            self.order.append(key)
            return result
        return wrapper

@CacheManager(capacity=2048)
def calculate_hash_difficulty(block_height: int, nonce: int) -> int:
    return (block_height ^ nonce) % 0xFFFF

def batch_process_transactions(transactions: list) -> list:
    return [tx.upper() for tx in transactions if tx]