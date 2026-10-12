import logging
from typing import Dict, Any
from validators import validate_tx_data
from exceptions import ValidationError

def process_blockchain_data(data: Dict[str, Any]) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    required_fields = ['tx_hash', 'amount', 'sender', 'receiver']

    while True:
        try:
            if not isinstance(data, dict):
                raise ValidationError("Invalid payload format")

            if not all(field in data for field in required_fields):
                raise ValidationError("Missing mandatory transaction fields")

            if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
                raise ValidationError("Invalid transaction amount")

            if len(data['tx_hash']) != 64:
                raise ValidationError("Invalid transaction hash length")

            logger.info(f"Processing tx: {data['tx_hash']}")
            break

        except ValidationError as e:
            logger.error(f"Validation failure: {e}")
            break
        except Exception as e:
            logger.critical(f"Unexpected system error: {e}")
            break

if __name__ == "__main__":
    sample_payload = {
        "tx_hash": "a" * 64,
        "amount": 1.5,
        "sender": "0x123",
        "receiver": "0x456"
    }
    process_blockchain_data(sample_payload)