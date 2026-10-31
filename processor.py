import re

class ProcessingError(Exception):
    pass

def validate_tx_hash(tx_hash: str) -> bool:
    return bool(re.fullmatch(r'0x[a-fA-F0-9]{64}', tx_hash))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def process_transactions(transactions: list):
    for tx in transactions:
        tx_hash = tx.get('hash')
        amount = tx.get('amount')

        if not validate_tx_hash(tx_hash):
            raise ProcessingError(f'Invalid tx format: {tx_hash}')
        
        if not validate_amount(amount):
            raise ProcessingError(f'Invalid amount: {amount}')
        
        execute_transfer(tx_hash, amount)

def execute_transfer(tx_hash: str, amount: float):
    print(f'Processing {tx_hash} for {amount} units')