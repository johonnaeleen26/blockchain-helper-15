import re
from typing import Optional

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    if chain_type == 'evm':
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
    if chain_type == 'btc':
        return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))
    return False

def validate_amount(amount: str) -> bool:
    try:
        value = float(amount)
        return value >= 0
    except ValueError:
        return False

def sanitize_tx_hash(tx_hash: str) -> Optional[str]:
    clean_hash = tx_hash.strip().lower()
    if re.match(r'^0x[a-f0-9]{64}$', clean_hash):
        return clean_hash
    return None

def format_wei_to_eth(wei: int) -> float:
    return float(wei) / 10**18

def is_valid_gas_price(price: int) -> bool:
    return isinstance(price, int) and price > 0