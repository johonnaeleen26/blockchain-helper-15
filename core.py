import functools
import time
from typing import Any, Callable, Dict

CACHE: Dict[str, Any] = {}

class CoreEngine:
    def __init__(self, ttl: int = 60):
        self.ttl = ttl

    @staticmethod
    def memoize(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{kwargs}"
            if key in CACHE:
                return CACHE[key]
            result = func(*args, **kwargs)
            CACHE[key] = result
            return result
        return wrapper

    @memoize
    def fetch_node_status(self, node_id: str) -> dict:
        time.sleep(0.1)
        return {"node_id": node_id, "status": "synced", "timestamp": time.time()}

    def batch_process(self, data: list) -> list:
        return [self.fetch_node_status(item) for item in data]

def clear_cache() -> None:
    CACHE.clear()