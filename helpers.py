import hashlib
import secrets
from typing import Any, Dict

def generate_address() -> str:
    return '0x' + secrets.token_hex(20)

def compute_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def validate_transaction(tx: Dict[str, Any]) -> bool:
    required = {'sender', 'receiver', 'amount', 'nonce'}
    return all(key in tx for key in required)

def format_wei(amount: int) -> float:
    return amount / 10**18

def sign_payload(data: str, private_key: str) -> str:
    payload = f"{data}{private_key}"
    return compute_hash(payload)

def sanitize_input(val: str) -> str:
    return val.strip().lower()

def calculate_gas(limit: int, price: int) -> int:
    return limit * price