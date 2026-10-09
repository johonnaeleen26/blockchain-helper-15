import hashlib
import hmac
import time
from typing import Dict, Any

def generate_nonce() -> str:
    return str(int(time.time() * 1000))

def create_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict[str, Any]) -> str:
    return '&'.join([f'{k}={v}' for k, v in sorted(params.items())])

def validate_address(address: str, chain: str) -> bool:
    if chain == 'eth':
        return len(address) == 42 and address.startswith('0x')
    if chain == 'btc':
        return len(address) >= 26 and len(address) <= 35
    return False

def calculate_gas_fee(gas_price: int, gas_limit: int) -> float:
    return (gas_price * gas_limit) / 10**18