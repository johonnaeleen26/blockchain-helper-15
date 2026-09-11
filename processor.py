import logging
from typing import Any, Dict, Optional

class ProcessingError(Exception):
    pass

def process_transaction(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if data is None:
        raise ProcessingError("Transaction data is missing")
    
    required_fields = ['hash', 'amount', 'sender']
    if not all(field in data for field in required_fields):
        raise ProcessingError("Missing required transaction fields")

    try:
        amount = float(data['amount'])
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return {"status": "success", "tx_hash": data['hash'], "processed": True}
    except (ValueError, TypeError) as e:
        logging.error(f"Invalid amount format: {e}")
        raise ProcessingError(f"Failed to parse transaction amount: {e}")

def safe_execute(data: Any) -> Optional[Dict[str, Any]]:
    try:
        return process_transaction(data)
    except ProcessingError as e:
        logging.error(f"Transaction processing halted: {e}")
        return None