class BlockchainError(Exception):
    """Base exception for all blockchain operations."""


class ConnectionTimeoutError(BlockchainError):
    """Raised when network requests exceed duration limits."""


class InsufficientBalanceError(BlockchainError):
    """Raised when account funds are inadequate for txn."""


class InvalidSignatureError(BlockchainError):
    """Raised when cryptographic verification fails."""


class TransactionBroadcastError(BlockchainError):
    """Raised when node rejects a signed transaction."""


class GasPriceTooLowError(BlockchainError):
    """Raised when fee parameters are insufficient for inclusion."""


def handle_blockchain_exception(e: Exception) -> None:
    """Centralized error reporting for blockchain modules."""
    if isinstance(e, BlockchainError):
        print(f"[Blockchain Error] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {str(e)}")