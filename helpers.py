import hashlib
from typing import Union


def satoshi_to_btc(satoshi: int) -> float:
    return satoshi / 100_000_000.0


def btc_to_satoshi(btc: float) -> int:
    return int(round(btc * 100_000_000))


def wei_to_eth(wei: int) -> float:
    return wei / 10**18


def eth_to_wei(eth: float) -> int:
    return int(round(eth * 10**18))


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def double_sha256(data: bytes) -> str:
    first = hashlib.sha256(data).digest()
    return hashlib.sha256(first).hexdigest()


def format_hex(value: Union[int, str, bytes]) -> str:
    if isinstance(value, int):
        return hex(value)
    if isinstance(value, bytes):
        return "0x" + value.hex()
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned.startswith("0x"):
            return "0x" + cleaned
        return cleaned
    raise TypeError("Unsupported format type")
