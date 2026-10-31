import hashlib
import re
from decimal import Decimal, ROUND_DOWN

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def normalize_hex(hex_str: str) -> str:
    cleaned = hex_str.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if len(cleaned) % 2 != 0:
        cleaned = "0" + cleaned
    return f"0x{cleaned}"


def to_checksum_address(address: str) -> str:
    if not ETH_ADDRESS_PATTERN.match(address):
        raise ValueError(f"Invalid Ethereum address: {address}")
    addr_lower = address.lower().replace("0x", "")
    hashed = hashlib.sha3_256(addr_lower.encode("utf-8")).hexdigest()
    checksum = "0x"
    for i, char in enumerate(addr_lower):
        if char.isdigit():
            checksum += char
        elif int(hashed[i], 16) >= 8:
            checksum += char.upper()
        else:
            checksum += char.lower()
    return checksum


def wei_to_ether(wei: int) -> Decimal:
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return (Decimal(wei) / Decimal(10**18)).quantize(
        Decimal("0.000000000000000001"), rounding=ROUND_DOWN
    )


def ether_to_wei(ether: str | float | Decimal) -> int:
    val = Decimal(str(ether))
    if val < 0:
        raise ValueError("Ether amount cannot be negative")
    return int(val * Decimal(10**18))


def format_tx_hash(tx_hash: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if not tx_hash.startswith("0x") or len(tx_hash) < (prefix_len + suffix_len + 2):
        return tx_hash
    return f"{tx_hash[:prefix_len]}...{tx_hash[-suffix_len:]}"
