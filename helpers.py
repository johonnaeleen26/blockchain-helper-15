import hashlib
from decimal import Decimal
from typing import Union

WEI_IN_ETHER = Decimal("1000000000000000000")
GWEI_IN_ETHER = Decimal("1000000000")


def wei_to_ether(wei: Union[int, str]) -> Decimal:
    return Decimal(str(wei)) / WEI_IN_ETHER


def ether_to_wei(ether: Union[float, str, Decimal]) -> int:
    return int(Decimal(str(ether)) * WEI_IN_ETHER)


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address.startswith("0x") or len(address) <= (leading + trailing):
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def calculate_tx_fee_eth(gas_used: int, gas_price_gwei: Union[int, float, Decimal]) -> Decimal:
    gwei_amount = Decimal(str(gas_price_gwei))
    return (Decimal(gas_used) * gwei_amount) / GWEI_IN_ETHER


def is_valid_address(address: str) -> bool:
    if not isinstance(address, str) or not address.startswith("0x"):
        return False
    if len(address) != 42:
        return False
    try:
        int(address[2:], 16)
        return True
    except ValueError:
        return False


def hex_to_int(hex_str: str) -> int:
    return int(hex_str.strip(), 16)
