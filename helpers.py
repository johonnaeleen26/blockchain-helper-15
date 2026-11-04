import hashlib
import hmac
from typing import Dict

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_address(address: str) -> str:
    if not address.startswith('0x'):
        return f'0x{address}'
    return address.lower()

def parse_units(amount: float, decimals: int = 18) -> int:
    return int(amount * (10**decimals))

def validate_tx_hash(tx_hash: str) -> bool:
    if len(tx_hash) != 66:
        return False
    try:
        int(tx_hash, 16)
        return True
    except ValueError:
        return False

def dict_to_query_string(params: Dict[str, str]) -> str:
    return '&'.join([f'{k}={v}' for k, v in params.items()])