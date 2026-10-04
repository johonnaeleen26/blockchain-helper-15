import decimal
from typing import Dict, Union

def normalize_amount(amount: Union[str, float, int]) -> decimal.Decimal:
    try:
        return decimal.Decimal(str(amount)).normalize()
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0')

def calculate_fee(amount: decimal.Decimal, rate: str) -> decimal.Decimal:
    fee_rate = decimal.Decimal(rate)
    return (amount * fee_rate).quantize(decimal.Decimal('0.00000001'))

def format_crypto_payload(tx_hash: str, value: str, recipient: str) -> Dict[str, str]:
    if not tx_hash.startswith('0x'):
        raise ValueError('Invalid transaction hash format')
    return {
        'hash': tx_hash.lower(),
        'value': str(normalize_amount(value)),
        'recipient': recipient.lower()
    }

def validate_balance_sufficiency(balance: str, required: str) -> bool:
    return decimal.Decimal(balance) >= decimal.Decimal(required)