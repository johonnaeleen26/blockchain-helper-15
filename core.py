import time
import functools
import requests
from typing import Callable, Any

def retry(retries: int = 3, delay: float = 1.0, exceptions=(requests.RequestException,)): 
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry(retries=3, delay=2.0)
def fetch_blockchain_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()