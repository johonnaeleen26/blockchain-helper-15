import re
from typing import Union

WEI_PER_ETH = 10**18
GWEI_PER_ETH = 10**9


def wei_to_eth(wei: int) -> float:
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei / WEI_PER_ETH


def eth_to_wei(eth: Union[int, float]) -> int:
    if eth < 0:
        raise ValueError("ETH amount cannot be negative")
    return int(eth * WEI_PER_ETH)


def truncate_address(address: str, chars: int = 4) -> str:
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid Ethereum address length")
    return f"{address[:chars + 2]}...{address[-chars:]}"


def is_valid_tx_hash(tx_hash: str) -> bool:
    return bool(re.match(r"^0x[a-fA-F0-9]{64}$", tx_hash))


def calculate_gas_fee_eth(gas_limit: int, gas_price_gwei: float) -> float:
    if gas_limit <= 0 or gas_price_gwei <= 0:
        raise ValueError("Gas parameters must be positive")
    total_gwei = gas_limit * gas_price_gwei
    return total_gwei / GWEI_PER_ETH
