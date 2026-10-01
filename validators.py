import re
from typing import Any, Union

EVM_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
TX_HASH_PATTERN = re.compile(r"^0x[a-fA-F0-9]{64}$")


def is_valid_evm_address(address: Any) -> bool:
    """Validate if the given input is a structurally valid EVM address.

    Args:
        address: The value to validate.

    Returns:
        True if valid EVM address string, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_PATTERN.match(address))


def is_valid_tx_hash(tx_hash: Any) -> bool:
    """Validate if the given input is a structurally valid Ethereum transaction hash.

    Args:
        tx_hash: The value to validate.

    Returns:
        True if valid transaction hash string, False otherwise.
    """
    if not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_PATTERN.match(tx_hash))


def validate_amount(amount: Union[int, float, str]) -> float:
    """Validate and convert crypto amount to float representation.

    Args:
        amount: The value to convert and validate.

    Raises:
        ValueError: If amount is negative or invalid format.

    Returns:
        The validated amount as a float.
    """
    try:
        parsed_amount = float(amount)
    except (ValueError, TypeError) as err:
        raise ValueError(f"Invalid numeric format: {amount}") from err

    if parsed_amount < 0:
        raise ValueError("Amount cannot be negative")

    return parsed_amount
