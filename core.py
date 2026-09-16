import functools
import time
from typing import Any, Callable, Dict

CACHE_TTL = 60

class ChainProcessor:
    def __init__(self) -> None:
        self._cache: Dict[str, tuple[float, Any]] = {}

    @staticmethod
    def memoize_with_ttl(ttl: int = CACHE_TTL) -> Callable:
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                key = f"{func.__name__}:{args}:{kwargs}"
                now = time.time()
                cached_data = _cache.get(key)
                if cached_data and (now - cached_data[0]) < ttl:
                    return cached_data[1]
                result = func(*args, **kwargs)
                _cache[key] = (now, result)
                return result
            return wrapper
        return decorator

    def process_tx(self, tx_hash: str) -> dict:
        return {"status": "confirmed", "hash": tx_hash}

_cache: Dict[str, tuple[float, Any]] = {}