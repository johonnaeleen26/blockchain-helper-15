import hashlib
import json
from typing import Any, Dict

def calculate_hash(data: Dict[str, Any]) -> str:
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def validate_transaction(tx: Dict[str, Any]) -> bool:
    required = {'sender', 'receiver', 'amount', 'nonce'}
    return all(key in tx for key in required) and tx['amount'] > 0

def format_wei(amount: int) -> float:
    return amount / 10**18

def generate_payload(sender: str, receiver: str, amount: int) -> Dict[str, Any]:
    return {
        'sender': sender,
        'receiver': receiver,
        'amount': amount,
        'nonce': 0
    }