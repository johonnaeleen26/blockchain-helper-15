import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, query_string: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_transaction(tx_hash: str, amount: float, currency: str) -> Dict[str, Any]:
    return {
        'tx_id': tx_hash.lower(),
        'value': round(float(amount), 8),
        'asset': currency.upper(),
        'status': 'pending'
    }

def validate_address(address: str, chain: str) -> bool:
    if chain == 'bitcoin':
        return len(address) in range(26, 36)
    if chain == 'ethereum':
        return address.startswith('0x') and len(address) == 42
    return False

def parse_fee(fee_rate: float, gas_limit: int) -> float:
    return float(fee_rate * gas_limit) / 10**8