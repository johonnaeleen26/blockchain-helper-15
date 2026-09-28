from typing import Union, List, Optional
import hashlib


def calculate_hash(data: str) -> str:
    """Generates a SHA-256 hash for the given input string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def format_wei(value: Union[int, float]) -> str:
    """Converts wei units to human-readable string representation."""
    return f"{value / 10**18:.18f}"


def validate_address(address: str) -> bool:
    """Checks if a string is a valid hexadecimal blockchain address."""
    return len(address) == 42 and address.startswith('0x')


def filter_transactions(txs: List[dict], min_val: float) -> List[dict]:
    """Returns transactions with values exceeding the specified threshold."""
    return [tx for tx in txs if tx.get('value', 0) >= min_val]


def get_network_config(network_id: Optional[int] = None) -> dict:
    """Retrieves RPC configuration based on network identifier."""
    configs = {
        1: {"rpc": "https://mainnet.infura.io", "chain_id": 1},
        137: {"rpc": "https://polygon-rpc.com", "chain_id": 137}
    }
    return configs.get(network_id or 1, {"rpc": "localhost", "chain_id": 0})