class BlockchainHelperError(Exception):
    """Base exception for blockchain-helper-15"""


class ConnectionError(BlockchainHelperError):
    """Raised when RPC connection fails"""


class ValidationError(BlockchainHelperError):
    """Raised when transaction data is malformed"""


class RateLimitError(BlockchainHelperError):
    """Raised when API rate limits are exceeded"""


class InsufficientFundsError(BlockchainHelperError):
    """Raised when account balance is too low"""


class TransactionTimeoutError(BlockchainHelperError):
    """Raised when transaction mining takes too long"""


class AuthenticationError(BlockchainHelperError):
    """Raised when API keys or signatures are invalid"""