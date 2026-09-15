import re

def validate_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    try:
        return isinstance(amount, (int, float)) and amount > 0
    except (ValueError, TypeError):
        return False

def validate_payload(data: dict) -> bool:
    required = {'address', 'amount', 'symbol'}
    if not isinstance(data, dict) or not required.issubset(data.keys()):
        return False
    return validate_address(data['address']) and validate_amount(data['amount'])

def process_stream(items: list):
    valid_items = []
    for item in items:
        if validate_payload(item):
            valid_items.append(item)
    return valid_items