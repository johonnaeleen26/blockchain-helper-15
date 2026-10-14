import hashlib
from typing import Optional

def generate_hash(data: str) -> str:
    """Produce sha256 hash string for input data."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def validate_address(address: str) -> bool:
    """Verify address format against standard constraints."""
    return len(address) == 42 and address.startswith('0x')

def format_wei_to_eth(wei: int) -> float:
    """Convert wei integer to eth float value."""
    return wei / 10**18

def get_chain_id(network: str) -> Optional[int]:
    """Map network name to integer chain identifier."""
    mapping = {
        'mainnet': 1,
        'goerli': 5,
        'sepolia': 11155111
    }
    return mapping.get(network.lower())

def sanitize_input(value: str) -> str:
    """Remove whitespace and strip prefix from hex."""
    clean = value.strip()
    return clean[2:] if clean.startswith('0x') else clean