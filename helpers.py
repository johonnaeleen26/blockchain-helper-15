import hashlib
import hmac
import time
from typing import Dict

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict) -> str:
    sorted_keys = sorted(params.keys())
    return '&'.join([f'{k}={params[k]}' for k in sorted_keys])

def get_timestamp() -> int:
    return int(time.time() * 1000)

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.isalnum()

def wei_to_ether(wei: int) -> float:
    return wei / 10**18

def ether_to_wei(ether: float) -> int:
    return int(ether * 10**18)