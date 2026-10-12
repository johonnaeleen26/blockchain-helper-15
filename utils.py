import re
from typing import Union

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_PATTERN = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$")

WEI_PER_ETH = 10**18
GWEI_PER_ETH = 10**9
SATOSHI_PER_BTC = 10**8


def wei_to_eth(wei_val: int) -> float:
    if wei_val < 0:
        raise ValueError("Wei value cannot be negative")
    return wei_val / WEI_PER_ETH


def eth_to_wei(eth_val: Union[int, float]) -> int:
    if eth_val < 0:
        raise ValueError("ETH value cannot be negative")
    return int(eth_val * WEI_PER_ETH)


def satoshi_to_btc(satoshi_val: int) -> float:
    if satoshi_val < 0:
        raise ValueError("Satoshi value cannot be negative")
    return satoshi_val / SATOSHI_PER_BTC


def btc_to_satoshi(btc_val: Union[int, float]) -> int:
    if btc_val < 0:
        raise ValueError("BTC value cannot be negative")
    return int(btc_val * SATOSHI_PER_BTC)


def is_valid_eth_address(address: str) -> bool:
    return bool(ETH_ADDRESS_PATTERN.match(address))


def is_valid_btc_address(address: str) -> bool:
    return bool(BTC_ADDRESS_PATTERN.match(address))


def format_tx_hash(tx_hash: str) -> str:
    clean_hash = tx_hash.lower()
    if not clean_hash.startswith("0x"):
        clean_hash = f"0x{clean_hash}"
    if len(clean_hash) != 66:
        raise ValueError("Invalid transaction hash length")
    return clean_hash
