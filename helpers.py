import time
import functools
from typing import Callable, Any

def retry_network_op(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError):
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(max_attempts=3, delay=2.0)
def fetch_blockchain_data(endpoint: str):
    # Simulate network operation
    import random
    if random.random() < 0.7:
        raise ConnectionError("node unreachable")
    return {"status": "success", "data": "0xabc123"}