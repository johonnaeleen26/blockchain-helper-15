import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"attempt {i+1} failed: {e}")
                    if i < attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator