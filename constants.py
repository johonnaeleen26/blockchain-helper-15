from typing import Final

# Network constants
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# Crypto optimization parameters
BATCH_SIZE: Final[int] = 1000
CACHE_SIZE: Final[int] = 512

# Gas estimation
GAS_LIMIT_BUFFER: Final[float] = 1.2
MIN_GAS_PRICE_GWEI: Final[int] = 5

# Node endpoints
NODE_SYNC_INTERVAL: Final[int] = 5
REQUEST_CONCURRENCY_LIMIT: Final[int] = 10

# Block constants
CONFIRMATION_THRESHOLD: Final[int] = 6
POLLING_INTERVAL_SECONDS: Final[float] = 0.5

# Database keys
DB_PREFIX: Final[str] = 'bch15_'
INDEX_MEMORY_LIMIT: Final[int] = 1024 * 1024 * 128