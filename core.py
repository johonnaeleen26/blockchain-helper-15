import re
from hashlib import sha256
from typing import Union


def wei_to_ether(wei: int) -> float:
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei / 10**18


def ether_to_wei(ether: Union[int, float]) -> int:
    if ether < 0:
        raise ValueError("Ether amount cannot be negative")
    return int(ether * 10**18)


def satoshi_to_btc(satoshi: int) -> float:
    if satoshi < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return satoshi / 10**8


def btc_to_satoshi(btc: Union[int, float]) -> int:
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(btc * 10**8)


def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(re.match(r"^(0x)?[0-9a-fA-F]{64}$", tx_hash))


def double_sha256(data: bytes) -> str:
    return sha256(sha256(data).digest()).hexdigest()
