class BlockchainValidationError(Exception):
    pass


def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        raise BlockchainValidationError("address must be a string")
    if len(address) != 42 or not address.startswith("0x"):
        raise BlockchainValidationError("invalid ethereum address format")
    if not all(c in "0123456789abcdefABCDEF" for c in address[2:]):
        raise BlockchainValidationError("address contains invalid characters")
    return True


def validate_amount(amount: float) -> bool:
    if not isinstance(amount, (int, float)):
        raise BlockchainValidationError("amount must be numeric")
    if amount <= 0:
        raise BlockchainValidationError("amount must be positive")
    return True


def validate_transaction(tx_data: dict) -> bool:
    required_fields = {"sender", "recipient", "amount"}
    if not isinstance(tx_data, dict):
        raise BlockchainValidationError("transaction must be a dictionary")
    if not required_fields.issubset(tx_data.keys()):
        missing = required_fields - tx_data.keys()
        raise BlockchainValidationError(f"missing fields: {missing}")
    
    validate_address(tx_data["sender"])
    validate_address(tx_data["recipient"])
    validate_amount(tx_data["amount"])
    return True