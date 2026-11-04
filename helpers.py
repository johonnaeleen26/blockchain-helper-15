import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_currency(value: float, precision: int = 8) -> str:
    return f"{value:.{precision}f}"

def validate_payload(data: Dict[str, Any], required: list) -> bool:
    return all(key in data for key in required)

def sanitize_address(address: str) -> str:
    return address.strip().lower()

def batch_process(items: list, chunk_size: int = 10):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]