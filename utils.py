import hashlib
import hmac
import time
from typing import Any, Dict

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict[str, Any]) -> str:
    sorted_keys = sorted(params.keys())
    return '&'.join([f"{k}={params[k]}" for k in sorted_keys])

def get_timestamp_ms() -> int:
    return int(time.time() * 1000)

def validate_address(address: str) -> bool:
    if not address or len(address) < 26:
        return False
    return address.isalnum()

def to_wei(amount: float, decimals: int = 18) -> int:
    return int(amount * (10 ** decimals))