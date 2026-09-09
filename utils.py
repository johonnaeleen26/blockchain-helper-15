import re
from decimal import Decimal, localcontext
from typing import Union

ADDR_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")


def to_base_unit(amount: Union[int, float, str, Decimal], decimals: int) -> int:
    with localcontext() as ctx:
        ctx.prec = 36
        return int(Decimal(str(amount)) * (Decimal(10) ** decimals))


def from_base_unit(amount: int, decimals: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 36
        return Decimal(amount) / (Decimal(10) ** decimals)


def is_valid_evm_address(address: str) -> bool:
    return bool(ADDR_RE.match(address))


def format_crypto_val(amount: Decimal, max_decimals: int = 6) -> str:
    val_str = f"{amount:f}"
    if "." in val_str:
        parts = val_str.split(".")
        if len(parts[1]) > max_decimals:
            return f"{amount:.{max_decimals}f}".rstrip("0").rstrip(".")
        return val_str.rstrip("0").rstrip(".")
    return val_str
