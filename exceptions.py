class BlockchainHelperError(Exception):
    """Base exception for the blockchain-helper-15 package."""


class ConnectionTimeoutError(BlockchainHelperError):
    """Raised when the blockchain node fails to respond."""


class InsufficientBalanceError(BlockchainHelperError):
    """Raised when account balance is too low for transaction."""


class InvalidAddressError(BlockchainHelperError):
    """Raised when an address fails format validation."""


class TransactionRevertedError(BlockchainHelperError):
    """Raised when a transaction fails on-chain."""


class SerializationError(BlockchainHelperError):
    """Raised during encoding or decoding failures."""


def raise_for_status(status_code: int, message: str) -> None:
    if status_code == 408:
        raise ConnectionTimeoutError(message)
    if status_code == 402:
        raise InsufficientBalanceError(message)
    if status_code == 400:
        raise InvalidAddressError(message)
    if status_code == 422:
        raise TransactionRevertedError(message)
    if status_code >= 400:
        raise BlockchainHelperError(f"Error {status_code}: {message}")