class BlockchainHelperError(Exception):
    """Base exception for blockchain-helper-15."""


class ConnectionError(BlockchainHelperError):
    """Raised when network communication fails."""


class ValidationError(BlockchainHelperError):
    """Raised when data validation fails."""


class InsufficientFundsError(BlockchainHelperError):
    """Raised during transaction processing failures."""


class ConfigurationError(BlockchainHelperError):
    """Raised when environment settings are invalid."""


class TimeoutError(BlockchainHelperError):
    """Raised when a request exceeds time limits."""