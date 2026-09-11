import hashlib
from decimal import Decimal
from typing import Union

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def encode_base58(data: bytes) -> str:
    num = int.from_bytes(data, byteorder="big")
    encoded = []
    while num > 0:
        num, remainder = divmod(num, 58)
        encoded.append(BASE58_ALPHABET[remainder])
    for byte in data:
        if byte == 0:
            encoded.append(BASE58_ALPHABET[0])
        else:
            break
    return "".join(reversed(encoded))


def decode_base58(s: str) -> bytes:
    num = 0
    for char in s:
        num = num * 58 + BASE58_ALPHABET.index(char)
    combined = bytearray()
    while num > 0:
        num, remainder = divmod(num, 256)
        combined.append(remainder)
    combined.reverse()
    pad = 0
    for char in s:
        if char == BASE58_ALPHABET[0]:
            pad += 1
        else:
            break
    return bytes(pad) + bytes(combined)


def to_wei(amount: Union[int, float, Decimal], unit: str = "ether") -> int:
    units = {"ether": 18, "gwei": 9, "wei": 0}
    if unit not in units:
        raise ValueError(f"Unknown unit: {unit}")
    return int(Decimal(str(amount)) * (10 ** units[unit]))


def from_wei(amount: int, unit: str = "ether") -> Decimal:
    units = {"ether": 18, "gwei": 9, "wei": 0}
    if unit not in units:
        raise ValueError(f"Unknown unit: {unit}")
    return Decimal(amount) / (10 ** units[unit])
