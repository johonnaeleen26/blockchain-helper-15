"""Cryptocurrency and blockchain network constant definitions."""

from typing import Dict, Final

# Chain IDs for major EVM networks
ETH_MAINNET: Final[int] = 1
BSC_MAINNET: Final[int] = 56
POLYGON_MAINNET: Final[int] = 137
ARBITRUM_MAINNET: Final[int] = 42161
OPTIMISM_MAINNET: Final[int] = 10

# Average block production times in seconds
BLOCK_TIMES: Final[Dict[int, float]] = {
    ETH_MAINNET: 12.0,
    BSC_MAINNET: 3.0,
    POLYGON_MAINNET: 2.0,
    ARBITRUM_MAINNET: 0.25,
    OPTIMISM_MAINNET: 2.0,
}

# Standard gas limits for EVM transactions
STANDARD_GAS_LIMIT: Final[int] = 21000
ERC20_TRANSFER_GAS_LIMIT: Final[int] = 65000

# Default token decimal precisions
TOKEN_DECIMALS: Final[Dict[str, int]] = {
    "ETH": 18,
    "BTC": 8,
    "USDT": 6,
    "USDC": 6,
    "DAI": 18,
}
