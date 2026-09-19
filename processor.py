import functools
import json
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: tuple = (urllib.error.URLError, TimeoutError),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator


class BlockchainProcessor:
    def __init__(self, rpc_url: str):
        self.rpc_url = rpc_url

    @retry_network_op(max_retries=4, backoff_factor=2.0)
    def fetch_latest_block(self) -> Dict[str, Any]:
        payload = json.dumps({
            "jsonrpc": "2.0",
            "method": "eth_blockNumber",
            "params": [],
            "id": 1
        }).encode("utf-8")
        req = urllib.request.Request(
            self.rpc_url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))

    @retry_network_op(max_retries=3)
    def fetch_balance(self, address: str) -> Dict[str, Any]:
        payload = json.dumps({
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [address, "latest"],
            "id": 1
        }).encode("utf-8")
        req = urllib.request.Request(
            self.rpc_url,
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))
