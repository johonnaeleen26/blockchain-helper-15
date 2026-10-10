import hashlib
import json
from typing import Any, Dict

def generate_hash(data: Dict[str, Any]) -> str:
    serialized = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(serialized).hexdigest()

def validate_transaction(tx: Dict[str, Any]) -> bool:
    required_fields = {'sender', 'receiver', 'amount', 'nonce'}
    return all(field in tx for field in required_fields)

def format_address(address: str) -> str:
    return address.strip().lower()

def batch_process(items: list, func: callable) -> list:
    return [func(item) for item in items]

def calculate_fee(amount: float, rate: float = 0.001) -> float:
    return round(amount * rate, 8)

class DataProcessor:
    @staticmethod
    def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in payload.items() if v is not None}

    @staticmethod
    def to_wei(amount: float) -> int:
        return int(amount * 10**18)

    @staticmethod
    def from_wei(amount: int) -> float:
        return amount / 10**18