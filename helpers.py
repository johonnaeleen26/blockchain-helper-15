import hashlib
import secrets
from typing import Union

def generate_keypair() -> tuple[str, str]:
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def validate_address(address: str) -> bool:
    return len(address) == 64 and all(c in '0123456789abcdef' for c in address)

def format_wei(value: Union[int, float]) -> float:
    return value / 10**18

def create_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def normalize_address(address: str) -> str:
    return address.lower().strip()

def sign_data(private_key: str, data: str) -> str:
    payload = f"{private_key}{data}".encode()
    return hashlib.sha256(payload).hexdigest()