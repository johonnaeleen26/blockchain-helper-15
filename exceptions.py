class BlockchainError(Exception):
    """Base exception for blockchain-helper-15."""

class ConnectionError(BlockchainError):
    """Raised when network connection fails."""

class ValidationError(BlockchainError):
    """Raised when data fails integrity checks."""

class TransactionError(BlockchainError):
    """Raised during transaction processing failures."""

class InsufficientFundsError(TransactionError):
    """Raised when wallet balance is too low."""

class RateLimitError(BlockchainError):
    """Raised when API rate limits are exceeded."""

class TimeoutError(BlockchainError):
    """Raised when an operation times out."""