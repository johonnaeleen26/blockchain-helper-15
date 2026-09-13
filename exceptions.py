class BlockchainHelperError(Exception):
    """Base exception for blockchain-helper library."""


class NodeConnectionError(BlockchainHelperError):
    """Raised when connection to the blockchain node fails."""

    def __init__(self, endpoint: str, message: str = "Failed to connect to node"):
        self.endpoint = endpoint
        self.message = f"{message}: {endpoint}"
        super().__init__(self.message)


class InvalidAddressError(BlockchainHelperError):
    """Raised when a blockchain address format is invalid."""

    def __init__(self, address: str, network: str):
        self.address = address
        self.network = network
        self.message = f"Invalid address '{address}' for network '{network}'"
        super().__init__(self.message)


class TransactionError(BlockchainHelperError):
    """Raised when a transaction fails or is rejected."""

    def __init__(self, tx_hash: str, reason: str):
        self.tx_hash = tx_hash
        self.reason = reason
        self.message = f"Transaction {tx_hash} failed: {reason}"
        super().__init__(self.message)


class InsufficientFundsError(BlockchainHelperError):
    """Raised when account balance is too low for the transaction."""

    def __init__(self, required: float, available: float):
        self.required = required
        self.available = available
        self.message = (
            f"Insufficient funds: required {required}, available {available}"
        )
        super().__init__(self.message)
