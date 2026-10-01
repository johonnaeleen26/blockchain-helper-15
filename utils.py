import hashlib
from decimal import Decimal, ROUND_HALF_UP
from typing import Union


def calculate_sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def format_crypto_amount(amount: Union[str, float, Decimal], precision: int = 8) -> Decimal:
    factor = Decimal(10) ** -precision
    return Decimal(str(amount)).quantize(factor, rounding=ROUND_HALF_UP)


def validate_address_format(address: str, length: int = 42) -> bool:
    if not address.startswith('0x'):
        return False
    return len(address) == length and all(c in '0123456789abcdefABCDEF' for c in address[2:])


def wei_to_ether(wei: Union[int, str]) -> Decimal:
    return Decimal(wei) / Decimal(10**18)


def ether_to_wei(ether: Union[str, float, Decimal]) -> int:
    return int(Decimal(str(ether)) * 10**18)