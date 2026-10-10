from enum import Enum, unique
from typing import Final

@unique
class NetworkMode(Enum):
    MAINNET = 'mainnet'
    TESTNET = 'testnet'
    DEVNET = 'devnet'

MAX_RETRIES: Final[int] = 3
CACHE_TTL_SECONDS: Final[int] = 300
CHUNK_SIZE: Final[int] = 1024
RPC_TIMEOUT: Final[float] = 5.0

DEFAULT_HEADERS: Final[dict[str, str]] = {
    'Content-Type': 'application/json',
    'User-Agent': 'blockchain-helper-15/1.0'
}

SUPPORTED_CHAINS: Final[tuple[str, ...]] = ('ethereum', 'solana', 'bitcoin')

BATCH_LIMIT: Final[int] = 50
MIN_CONFIRMATIONS: Final[int] = 6

def get_timeout(network: NetworkMode) -> float:
    return RPC_TIMEOUT * (2 if network == NetworkMode.MAINNET else 1)