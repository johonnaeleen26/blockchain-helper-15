from decimal import Decimal, getcontext
from typing import Union
import hashlib

getcontext().prec = 28

def wei_to_ether(wei: Union[int, str]) -> Decimal:
    return Decimal(wei) / Decimal('1000000000000000000')

def ether_to_wei(ether: Union[float, str]) -> int:
    return int(Decimal(str(ether)) * Decimal('1000000000000000000'))

def calculate_sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def format_address(address: str) -> str:
    if not address.startswith('0x'):
        address = '0x' + address
    return address.lower()

def validate_gas_price(price: Union[int, float]) -> bool:
    return price > 0

def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]