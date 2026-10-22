import time
import functools
import requests
from typing import Callable, Any, Optional

def retry_operation(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, ConnectionError):
                    attempt += 1
                    if attempt >= retries:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=0.5)
def fetch_blockchain_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()