import hashlib
from decimal import Decimal
from typing import Union

WEI_PER_ETHER = Decimal("1000000000000000000")
SATOSHI_PER_BTC = Decimal("100000000")


def wei_to_ether(wei: Union[int, str, Decimal]) -> Decimal:
    return Decimal(str(wei)) / WEI_PER_ETHER


def ether_to_wei(ether: Union[int, float, str, Decimal]) -> int:
    return int(Decimal(str(ether)) * WEI_PER_ETHER)


def satoshi_to_btc(satoshi: Union[int, str, Decimal]) -> Decimal:
    return Decimal(str(satoshi)) / SATOSHI_PER_BTC


def btc_to_satoshi(btc: Union[int, float, str, Decimal]) -> int:
    return int(Decimal(str(btc)) * SATOSHI_PER_BTC)


def hex_to_bytes(hex_str: str) -> bytes:
    clean_hex = hex_str[2:] if hex_str.startswith("0x") else hex_str
    if len(clean_hex) % 2 != 0:
        clean_hex = "0" + clean_hex
    return bytes.fromhex(clean_hex)


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def format_tx_hash(tx_hash: str) -> str:
    clean_hash = tx_hash.lower().strip()
    if not clean_hash.startswith("0x"):
        clean_hash = f"0x{clean_hash}"
    if len(clean_hash) != 66:
        raise ValueError("Invalid transaction hash length")
    return clean_hash
