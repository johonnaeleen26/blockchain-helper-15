import hashlib
import json
from typing import Any, Dict

def generate_hash(data: Dict[str, Any]) -> str:
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def validate_address(address: str) -> bool:
    return len(address) == 42 and address.startswith('0x')

def format_wei(value: int) -> float:
    return value / 10**18

def parse_transaction(raw_data: str) -> Dict[str, Any]:
    try:
        return json.loads(raw_data)
    except (ValueError, TypeError):
        return {}

def calculate_gas_cost(gas_limit: int, gas_price: int) -> int:
    return gas_limit * gas_price