class BlockchainError(Exception):
    """Base exception for blockchain-helper-15"""

class ConnectionTimeoutError(BlockchainError):
    """Raised when network requests exceed threshold"""

class ValidationError(BlockchainError):
    """Raised when data fails format constraints"""

class InsufficientFundsError(BlockchainError):
    """Raised when wallet balance is too low"""

class TransactionBroadcastError(BlockchainError):
    """Raised when transaction rejection occurs at node"""

def handle_blockchain_exception(e: Exception) -> str:
    if isinstance(e, ConnectionTimeoutError):
        return "NETWORK_RETRY_REQUIRED"
    if isinstance(e, ValidationError):
        return "INVALID_DATA_STRUCTURE"
    if isinstance(e, InsufficientFundsError):
        return "USER_ACTION_REQUIRED"
    if isinstance(e, TransactionBroadcastError):
        return "REJECTED_BY_NODE"
    return "INTERNAL_SYSTEM_FAILURE"