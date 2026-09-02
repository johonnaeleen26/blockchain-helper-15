import time
import requests
from functools import wraps

def retry(max_retries=3, backoff=1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(backoff * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

class NetworkHandler:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    @retry(max_retries=5, backoff=0.5)
    def fetch_data(self, method, params):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        response = requests.post(self.endpoint, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise Exception(data["error"])
        return data["result"]

    @retry(max_retries=3, backoff=1.0)
    def get_balance(self, address):
        return self.fetch_data("eth_getBalance", [address, "latest"])

    @retry(max_retries=3, backoff=1.0)
    def get_transaction(self, tx_hash):
        return self.fetch_data("eth_getTransactionByHash", [tx_hash])