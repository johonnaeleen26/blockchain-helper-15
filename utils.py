import hashlib
import json
from typing import Any, Dict

def calculate_hash(data: Dict[str, Any]) -> str:
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def format_wei_to_ether(wei: int) -> float:
    return float(wei) / 10**18

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or len(address) != 42:
        return False
    return address.startswith('0x') and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def sanitize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}

def hex_to_int(hex_val: str) -> int:
    return int(hex_val, 16)

def create_response(status: str, data: Any = None) -> Dict[str, Any]:
    return {
        'status': status,
        'payload': data,
        'version': '1.0.0'
    }