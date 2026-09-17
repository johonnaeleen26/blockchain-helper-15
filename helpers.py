import hashlib
import re

SATOSHI_PER_BTC = 100_000_000
TXID_PATTERN = re.compile(r"^[a-fA-F0-9]{64}$")


def satoshi_to_btc(satoshi: int) -> float:
    if satoshi < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return satoshi / SATOSHI_PER_BTC


def btc_to_satoshi(btc: float) -> int:
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return round(btc * SATOSHI_PER_BTC)


def is_valid_txid(txid: str) -> bool:
    if not isinstance(txid, str):
        return False
    return bool(TXID_PATTERN.match(txid))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()
