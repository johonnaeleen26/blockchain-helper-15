import re

def validate_address(address: str) -> bool:
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: str) -> bool:
    try:
        return float(amount) > 0
    except ValueError:
        return False

def validate_tx_data(data: dict) -> bool:
    required_fields = ['sender', 'receiver', 'amount', 'gas_limit']
    if not all(field in data for field in required_fields):
        return False
    
    if not validate_address(data['sender']) or not validate_address(data['receiver']):
        return False
    
    if not validate_amount(str(data['amount'])):
        return False
        
    return isinstance(data['gas_limit'], int) and data['gas_limit'] > 21000

def process_input(raw_data: dict) -> dict:
    if not validate_tx_data(raw_data):
        raise ValueError('invalid transaction data format')
    return raw_data