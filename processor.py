import hashlib
import json
from typing import Any, Dict

def hash_data(data: Dict[str, Any]) -> str:
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def validate_transaction(tx: Dict[str, Any]) -> bool:
    required = {'sender', 'recipient', 'amount'}
    return all(key in tx for key in required)

def format_currency(amount: float, precision: int = 8) -> str:
    return f"{amount:.{precision}f}"

def aggregate_balances(transactions: list[Dict[str, Any]]) -> Dict[str, float]:
    balances = {}
    for tx in transactions:
        sender = tx['sender']
        recipient = tx['recipient']
        amount = float(tx['amount'])
        
        balances[sender] = balances.get(sender, 0.0) - amount
        balances[recipient] = balances.get(recipient, 0.0) + amount
    return balances

def create_block_header(index: int, prev_hash: str, nonce: int) -> Dict[str, Any]:
    return {
        'index': index,
        'previous_hash': prev_hash,
        'nonce': nonce
    }