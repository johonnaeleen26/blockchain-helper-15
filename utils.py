import time
import functools
from typing import Callable, Any

MAX_RETRIES = 3
RETRY_DELAY = 1.0

def retry_network_op(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        attempts = 0
        while attempts < MAX_RETRIES:
            try:
                return func(*args, **kwargs)
            except (ConnectionError, TimeoutError) as e:
                attempts += 1
                if attempts == MAX_RETRIES:
                    raise e
                time.sleep(RETRY_DELAY * attempts)
        return None
    return wrapper