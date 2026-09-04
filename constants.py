from typing import Dict, Final

# Chain IDs
ETH_MAINNET: Final[int] = 1
SEPOLIA: Final[int] = 11155111
BSC_MAINNET: Final[int] = 56
POLYGON_MAINNET: Final[int] = 137
ARBITRUM_ONE: Final[int] = 42161
OPTIMISM: Final[int] = 10

# RPC Methods
RPC_GET_BALANCE: Final[str] = "eth_getBalance"
RPC_SEND_RAW_TRANSACTION: Final[str] = "eth_sendRawTransaction"
RPC_GET_TRANSACTION_RECEIPT: Final[str] = "eth_getTransactionReceipt"
RPC_BLOCK_NUMBER: Final[str] = "eth_blockNumber"
RPC_ESTIMATE_GAS: Final[str] = "eth_estimateGas"

# Standard Gas Limits
GAS_LIMIT_ETH: Final[int] = 21000
GAS_LIMIT_ERC20: Final[int] = 65000

# Explorer URLs
EXPLORER_URLS: Final[Dict[int, str]] = {
    ETH_MAINNET: "https://etherscan.io",
    SEPOLIA: "https://sepolia.etherscan.io",
    BSC_MAINNET: "https://bscscan.com",
    POLYGON_MAINNET: "https://polygonscan.com",
    ARBITRUM_ONE: "https://arbiscan.io",
    OPTIMISM: "https://optimistic.etherscan.io",
}

# Timeouts and Retries
DEFAULT_TIMEOUT: Final[float] = 10.0
MAX_RETRIES: Final[int] = 3
RETRY_BACKOFF_FACTOR: Final[float] = 0.5
