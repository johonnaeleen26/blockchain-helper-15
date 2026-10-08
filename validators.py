import re
from typing import Union


def is_valid_eth_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash))


def is_valid_hex_string(val: str, length: Union[int, None] = None) -> bool:
    if not isinstance(val, str) or not val.startswith("0x"):
        return False
    hex_body = val[2:]
    if length is not None and len(hex_body) != length:
        return False
    return bool(re.match(r"^[a-fA-F0-9]*$", hex_body))


def validate_block_number(block: Union[int, str]) -> bool:
    if isinstance(block, int):
        return block >= 0
    if isinstance(block, str):
        if block.startswith("0x"):
            try:
                return int(block, 16) >= 0
            except ValueError:
                return False
        return block.isdigit()
    return False
