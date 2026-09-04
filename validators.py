import re
from typing import Union

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_eth_address(address: str) -> bool:
    return bool(ADDRESS_PATTERN.match(address))

def format_wei_to_eth(wei: Union[int, str]) -> float:
    try:
        return float(wei) / 10**18
    except (ValueError, TypeError):
        return 0.0

def sanitize_currency_pair(pair: str) -> str:
    return pair.strip().upper().replace('/', '_')

def is_valid_transaction_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str) or len(tx_hash) != 66:
        return False
    return tx_hash.startswith('0x') and all(c in '0123456789abcdefABCDEF' for c in tx_hash[2:])