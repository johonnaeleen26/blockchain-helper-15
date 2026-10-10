import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, message: str) -> str:
    """Create HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict[str, Any]) -> str:
    """Serialize dictionary parameters for blockchain transaction signing."""
    return '&'.join([f"{k}={v}" for k, v in sorted(params.items())])

def validate_address(address: str) -> bool:
    """Check if address length and format match standard blockchain specs."""
    if not isinstance(address, str) or len(address) < 26:
        return False
    return address.isalnum()

def convert_wei_to_eth(wei_amount: int) -> float:
    """Convert smallest denomination to standard base unit."""
    return float(wei_amount) / 10**18