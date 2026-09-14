import logging
from typing import Any, Dict

def validate_transaction(tx: Dict[str, Any]) -> bool:
    required = {'sender', 'receiver', 'amount'}
    return all(key in tx for key in required) and isinstance(tx['amount'], (int, float))

def process_blockchain_data(data: list) -> None:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('blockchain-helper-15')

    for entry in data:
        if not isinstance(entry, dict):
            logger.error(f'Invalid data format: {type(entry)}')
            continue

        if not validate_transaction(entry):
            logger.warning(f'Schema validation failed for: {entry}')
            continue

        try:
            execute_transfer(entry)
        except Exception as e:
            logger.error(f'Transaction execution failure: {e}')

def execute_transfer(tx: Dict[str, Any]) -> None:
    print(f'Processing transfer of {tx["amount"]} to {tx["receiver"]}')

if __name__ == '__main__':
    sample_data = [
        {'sender': 'A', 'receiver': 'B', 'amount': 10.5},
        {'invalid': 'data'},
        {'sender': 'C', 'receiver': 'D', 'amount': 'high'}
    ]
    process_blockchain_data(sample_data)