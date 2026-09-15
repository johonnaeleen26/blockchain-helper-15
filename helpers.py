import json
from typing import Any, Dict, Optional

class BlockchainError(Exception):
    pass

def parse_tx_data(data: str) -> Dict[str, Any]:
    if not data or not isinstance(data, str):
        raise ValueError('Invalid transaction data format')

    try:
        decoded = json.loads(data)
    except json.JSONDecodeError as e:
        raise BlockchainError(f'Malformed transaction JSON: {e}') from e

    if 'txid' not in decoded or 'amount' not in decoded:
        raise KeyError('Missing required transaction fields')

    return decoded

def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return len(address) == 42 and address.startswith('0x')

def get_safe_tx_amount(data: str) -> float:
    try:
        tx = parse_tx_data(data)
        amount = float(tx.get('amount', 0))
        if amount < 0:
            raise ValueError('Negative transaction amount')
        return amount
    except (ValueError, KeyError, BlockchainError):
        return 0.0