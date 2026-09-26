import time
import functools
from typing import Callable, Any, Type

def retry_network_call(max_retries: int = 3, delay: float = 1.0, exceptions: tuple = (ConnectionError, TimeoutError)) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3)
def fetch_blockchain_data(endpoint: str) -> dict:
    # Simulate network call
    if not endpoint:
        raise ConnectionError("Failed to connect to node")
    return {"status": "ok", "data": "block_info"}