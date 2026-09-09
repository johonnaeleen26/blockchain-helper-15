class BlockchainError(Exception):
    """Base exception for blockchain-helper-15."""


class ConnectionTimeoutError(BlockchainError):
    """Raised when the blockchain node fails to respond."""


class InvalidTransactionError(BlockchainError):
    """Raised when transaction data fails validation."""


class InsufficientFundsError(BlockchainError):
    """Raised when the wallet balance is too low."""


class RateLimitExceededError(BlockchainError):
    """Raised when API request limits are breached."""


def raise_if_invalid(condition: bool, message: str) -> None:
    """Validate conditions and raise Transaction errors if false."""
    if not condition:
        raise InvalidTransactionError(message)


def handle_exception(exc: Exception) -> str:
    """Format exception messages for logging purposes."""
    if isinstance(exc, BlockchainError):
        return f"[Blockchain Error]: {str(exc)}"
    return f"[Unexpected Error]: {str(exc)}"