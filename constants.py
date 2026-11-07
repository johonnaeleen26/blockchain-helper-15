from typing import Final

CACHE_TTL: Final[int] = 300
MAX_RETRIES: Final[int] = 3
BLOCK_SIZE: Final[int] = 1024
RPC_TIMEOUT: Final[float] = 10.0

DATABASE_POOL_SIZE: Final[int] = 20
CONCURRENT_TASKS: Final[int] = 8

PRECISION_SCALE: Final[int] = 18

NETWORK_ENDPOINTS: Final[tuple[str, ...]] = (
    "https://mainnet.infura.io/v3/",
    "https://eth-mainnet.alchemyapi.io/v2/",
)

OPCODES: Final[dict[str, int]] = {
    "PUSH": 0x60,
    "POP": 0x50,
    "ADD": 0x01,
    "MUL": 0x02,
    "SUB": 0x03,
    "DIV": 0x04,
    "SDIV": 0x05,
    "MOD": 0x06,
    "SMOD": 0x07,
    "ADDMOD": 0x08,
    "MULMOD": 0x09,
    "EXP": 0x0a,
    "SIGNEXTEND": 0x0b,
    "LT": 0x10,
    "GT": 0x11,
    "SLT": 0x12,
    "SGT": 0x13,
    "EQ": 0x14,
    "ISZERO": 0x15,
    "AND": 0x16,
    "OR": 0x17,
    "XOR": 0x18,
    "NOT": 0x19,
    "BYTE": 0x1a,
}