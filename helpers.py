import re

ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

class ValidationError(Exception):
    pass

def validate_tx_data(data: dict) -> bool:
    if not isinstance(data.get('amount'), (int, float)) or data['amount'] <= 0:
        raise ValidationError('Invalid transaction amount')
    
    address = data.get('address')
    if not isinstance(address, str) or not ADDRESS_PATTERN.match(address):
        raise ValidationError('Invalid wallet address format')
    
    return True

def process_transactions(transactions: list):
    for tx in transactions:
        try:
            if validate_tx_data(tx):
                print(f'Processing {tx["amount"]} to {tx["address"]}')
        except ValidationError as e:
            print(f'Skipping invalid transaction: {e}')

if __name__ == '__main__':
    sample_data = [
        {'amount': 1.5, 'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F'},
        {'amount': -1, 'address': 'invalid_address'}
    ]
    process_transactions(sample_data)