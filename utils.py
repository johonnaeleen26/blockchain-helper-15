import time
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple, Union

logger = logging.getLogger("blockchain_helper.utils")

def retry(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = Exception,
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error("Function %s failed after %d attempts: %s", func.__name__, retries, e)
                        raise
                    logger.warning(
                        "Retrying %s in %.2fs (attempt %d/%d) due to error: %s",
                        func.__name__,
                        current_delay,
                        attempt,
                        retries,
                        e,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator