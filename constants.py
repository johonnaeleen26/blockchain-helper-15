from typing import Final

RPC_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
BLOCK_TIME_SEC: Final[float] = 12.0

HTTP_STATUS_OK: Final[int] = 200
HTTP_STATUS_BAD_REQUEST: Final[int] = 400
HTTP_STATUS_UNAUTHORIZED: Final[int] = 401
HTTP_STATUS_NOT_FOUND: Final[int] = 404
HTTP_STATUS_SERVER_ERROR: Final[int] = 500

GAS_PRICE_MULTIPLIER: Final[float] = 1.1
DEFAULT_CHAIN_ID: Final[int] = 1

SUPPORTED_NETWORKS: Final[tuple[str, ...]] = (
    "mainnet",
    "goerli",
    "sepolia",
    "polygon",
    "bsc"
)

ENV_VAR_PREFIX: Final[str] = "BC_HELPER_

CURRENCY_SYMBOL: Final[str] = "ETH"
DECIMALS: Final[int] = 18