import re
from typing import Optional


def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))


def validate_amount(amount: float) -> bool:
    """Validate transaction amount is positive."""
    return isinstance(amount, (int, float)) and amount > 0


def validate_chain_id(chain_id: int) -> bool:
    """Check for supported EVM chain identifiers."""
    supported_chains = {1, 56, 137, 42161}
    return chain_id in supported_chains


def sanitize_tx_hash(tx_hash: str) -> Optional[str]:
    """Sanitize transaction hash for database operations."""
    if not re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash):
        return None
    return tx_hash.lower()


def validate_gas_price(gas: float) -> bool:
    """Verify gas price within reasonable network limits."""
    return 0.000000001 <= gas <= 1.0