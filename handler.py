import logging
from typing import Any, Dict, Optional

REQUIRED_KEYS = {'tx_id', 'amount', 'sender', 'receiver'}

class ProcessingError(Exception):
    pass

def validate_transaction(data: Dict[str, Any]) -> bool:
    if not isinstance(data, dict):
        return False
    if not REQUIRED_KEYS.issubset(data.keys()):
        return False
    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return False
    return True

def process_blockchain_stream(stream: Any) -> None:
    for entry in stream:
        try:
            if not validate_transaction(entry):
                logging.warning(f"Invalid transaction format: {entry}")
                continue
            
            execute_transfer(entry)
            
        except Exception as e:
            logging.error(f"Unexpected processing failure: {e}")
            raise ProcessingError(f"Failed at tx {entry.get('tx_id')}") from e

def execute_transfer(tx: Dict[str, Any]) -> None:
    logging.info(f"Processing tx {tx['tx_id']}: {tx['amount']} units")