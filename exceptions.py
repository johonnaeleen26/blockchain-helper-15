class BlockchainError(Exception):
    """Base exception for all blockchain helper errors."""

    def __init__(self, message: str, code: int | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        if self.code is not None:
            return f"[{self.code}] {self.message}"
        return self.message


class InvalidAddressError(BlockchainError):
    """Raised when a blockchain address format is invalid."""


class InsufficientBalanceError(BlockchainError):
    """Raised when an account lacks required funds for a transaction."""

    def __init__(
        self, message: str, required: float, available: float
    ) -> None:
        super().__init__(message, code=402)
        self.required = required
        self.available = available


class TransactionFailedError(BlockchainError):
    """Raised when a transaction execution or broadcast fails."""

    def __init__(
        self, message: str, tx_hash: str | None = None, code: int = 500
    ) -> None:
        super().__init__(message, code=code)
        self.tx_hash = tx_hash


class NodeConnectionError(BlockchainError):
    """Raised when connection to an RPC node fails."""
