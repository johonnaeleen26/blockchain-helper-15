import re
from typing import Optional


def is_valid_eth_address(address: str) -> bool:
    """Check if the given string is a valid Ethereum address.

    Args:
        address: The address string to validate.

    Returns:
        True if valid hexadecimal address starting with 0x, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    """Validate a standard 32-byte transaction hash.

    Args:
        tx_hash: Transaction hash string.

    Returns:
        True if valid 64-character hex string with optional 0x prefix.
    """
    if not isinstance(tx_hash, str):
        return False
    pattern = r"^(0x)?[a-fA-F0-9]{64}$"
    return bool(re.match(pattern, tx_hash))


def is_valid_btc_address(address: str) -> bool:
    """Validate a legacy, SegWit, or Native SegWit Bitcoin address format.

    Args:
        address: Bitcoin address string.

    Returns:
        True if matches standard Bitcoin address regex patterns.
    """
    if not isinstance(address, str):
        return False
    pattern = r"^(1|3|bc1q|bc1p)[a-zA-HJ-NP-Z0-9]{25,62}$"
    return bool(re.match(pattern, address))


def validate_block_number(block_num: Optional[int]) -> bool:
    """Ensure block number is a non-negative integer.

    Args:
        block_num: Block number to check.

    Returns:
        True if valid non-negative integer, False otherwise.
    """
    if block_num is None:
        return False
    return isinstance(block_num, int) and block_num >= 0
