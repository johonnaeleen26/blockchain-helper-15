from typing import Dict, Any, Optional
import hashlib

def calculate_hash(data: Dict[str, Any]) -> str:
    """Generates a SHA-256 hash for a dictionary of blockchain data."""
    encoded_data = str(sorted(data.items())).encode()
    return hashlib.sha256(encoded_data).hexdigest()

def format_wei(value: int, decimals: int = 18) -> float:
    """Converts wei units to human-readable token amounts."""
    return float(value) / (10 ** decimals)

def validate_address(address: str) -> bool:
    """Checks if a string is a valid hexadecimal blockchain address."""
    if not address.startswith("0x") or len(address) != 42:
        return False
    return all(c in "0123456789abcdefABCDEF" for c in address[2:])

def get_gas_estimate(gas_limit: int, gas_price: int) -> int:
    """Calculates total transaction fee in wei."""
    return gas_limit * gas_price