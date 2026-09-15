import hashlib
import hmac
from typing import Dict, Any

class CryptoHelper:
    @staticmethod
    def generate_sha256(data: str) -> str:
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    @staticmethod
    def sign_payload(secret: str, payload: str) -> str:
        return hmac.new(
            secret.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def format_wei(amount: int, decimals: int = 18) -> float:
        return amount / (10 ** decimals)

    @staticmethod
    def validate_address(address: str) -> bool:
        if not address.startswith('0x') or len(address) != 42:
            return False
        return all(c in '0123456789abcdefABCDEF' for c in address[2:])

def get_nonce(timestamp: int) -> str:
    return hashlib.md5(str(timestamp).encode()).hexdigest()