import time
from typing import Any, List, Union


def wei_to_ether(wei: int) -> float:
    return wei / 10**18


def ether_to_wei(ether: Union[int, float]) -> int:
    return int(ether * 10**18)


def format_hex_prefix(hex_str: str) -> str:
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        return cleaned
    return f"0x{cleaned}"


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    address = format_hex_prefix(address)
    if len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def chunk_payload(items: List[Any], chunk_size: int) -> List[List[Any]]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def current_block_timestamp() -> int:
    return int(time.time())
