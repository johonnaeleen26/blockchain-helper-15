import re

def validate_address(address: str) -> bool:
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def process_input(data: dict) -> dict:
    address = data.get('address', '')
    amount = data.get('amount', 0)

    if not validate_address(address):
        raise ValueError(f'invalid blockchain address: {address}')

    if not validate_amount(amount):
        raise ValueError(f'invalid transaction amount: {amount}')

    return {'status': 'valid', 'data': data}

def main_loop(items: list):
    for item in items:
        try:
            validated = process_input(item)
            print(f'processing: {validated}')
        except (ValueError, TypeError) as e:
            print(f'skipped item: {e}')