class BlockchainError(Exception):
    """Base exception for all blockchain-related issues."""


class ConnectionTimeoutError(BlockchainError):
    """Raised when the node fails to respond."""


class InsufficientFundsError(BlockchainError):
    """Raised when wallet balance is too low."""


class TransactionValidationError(BlockchainError):
    """Raised when transaction data is malformed."""


class NetworkSyncError(BlockchainError):
    """Raised when block headers are out of sync."""


def raise_if_invalid(condition: bool, message: str, exception_type: type = BlockchainError) -> None:
    """Utility to trigger domain-specific exceptions."""
    if not condition:
        raise exception_type(message)