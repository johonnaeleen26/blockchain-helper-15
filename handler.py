import json
import time
import urllib.error
import urllib.request
from functools import wraps
from typing import Any, Callable, Dict, Optional


class NetworkError(Exception):
    pass


def retry_network_op(max_retries: int = 3, backoff_factor: float = 0.5):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            delay = backoff_factor
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (urllib.error.URLError, TimeoutError, OSError) as err:
                    if attempt == max_retries:
                        raise NetworkError(f"Failed after {max_retries} attempts: {err}") from err
                    time.sleep(delay)
                    delay *= 2
        return wrapper
    return decorator


class RPCRequestHandler:
    def __init__(self, endpoint_url: str, timeout: int = 10):
        self.endpoint_url = endpoint_url
        self.timeout = timeout

    @retry_network_op(max_retries=4, backoff_factor=0.5)
    def send_rpc_request(self, method: str, params: Optional[list] = None) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1,
        }
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            self.endpoint_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
            if "error" in result:
                raise NetworkError(f"RPC error payload received: {result['error']}")
            return result.get("result")
