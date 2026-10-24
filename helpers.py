import re
from typing import Union


def wei_to_ether(wei: int) -> float:
    return wei / 10**18


def ether_to_wei(ether: Union[int, float]) -> int:
    return int(ether * 10**18)


def gwei_to_wei(gwei: Union[int, float]) -> int:
    return int(gwei * 10**9)


def truncate_address(address: str, chars: int = 4) -> str:
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid Ethereum address format")
    return f"{address[:chars + 2]}...{address[-chars:]}"


def calculate_gas_fee_eth(gas_limit: int, gas_price_gwei: float) -> float:
    wei_price = gwei_to_wei(gas_price_gwei)
    return wei_to_ether(gas_limit * wei_price)


def is_hex_string(value: str) -> bool:
    if value.startswith("0x"):
        value = value[2:]
    return bool(re.fullmatch(r"[0-9a-fA-F]+", value))
