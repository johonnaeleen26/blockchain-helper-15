class BlockchainError(Exception):
    """Base exception for blockchain-helper-15 operations."""

class ConnectionError(BlockchainError):
    """Raised when network connection to node fails."""

class ValidationError(BlockchainError):
    """Raised when data validation fails."""

class TransactionError(BlockchainError):
    """Raised when transaction signing or broadcast fails."""

class InsufficientFundsError(TransactionError):
    """Raised when account balance is insufficient for operation."""

class RateLimitError(BlockchainError):
    """Raised when API rate limit is exceeded."""

class ConfigurationError(BlockchainError):
    """Raised when node configuration is invalid."""

def raise_if_invalid(condition: bool, message: str) -> None:
    """Raise ValidationError if condition is False."""
    if not condition:
        raise ValidationError(message)

def handle_rpc_error(code: int, message: str) -> None:
    """Route raw RPC errors to specific exceptions."""
    if code == -32000:
        raise InsufficientFundsError(message)
    elif code == 429:
        raise RateLimitError(message)
    else:
        raise BlockchainError(f"RPC error {code}: {message}")