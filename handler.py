import re
def is_valid_address(address):
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
def is_valid_amount(amount):
    if not isinstance(amount, (int, float)):
        return False
    return amount > 0
def is_valid_hash(tx_hash):
    if not isinstance(tx_hash, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{64}$', tx_hash))
def main_processing_loop(data):
    processed = []
    for item in data:
        if not isinstance(item, dict):
            processed.append({'status': 'error', 'reason': 'invalid input type'})
            continue
        sender = item.get('sender')
        recipient = item.get('recipient')
        amount = item.get('amount')
        tx_hash = item.get('tx_hash')
        if not is_valid_address(sender):
            processed.append({'status': 'invalid', 'reason': 'bad sender address'})
            continue
        if not is_valid_address(recipient):
            processed.append({'status': 'invalid', 'reason': 'bad recipient address'})
            continue
        if not is_valid_amount(amount):
            processed.append({'status': 'invalid', 'reason': 'bad amount'})
            continue
        if tx_hash and not is_valid_hash(tx_hash):
            processed.append({'status': 'invalid', 'reason': 'bad tx hash'})
            continue
        result = {'status': 'processed', 'sender': sender, 'recipient': recipient, 'amount': amount, 'tx_hash': tx_hash}
        processed.append(result)
    return processed
if __name__ == '__main__':
    sample_data = [{'sender': '0x1234567890123456789012345678901234567890', 'recipient': '0x0987654321098765432109876543210987654321', 'amount': 10.5, 'tx_hash': '0x' + 'a'*64}, {'sender': '0x1234567890123456789012345678901234567890', 'recipient': 'invalid', 'amount': 5}, {'sender': '0x1234567890123456789012345678901234567890', 'recipient': '0x0987654321098765432109876543210987654321', 'amount': -1}, 'not a dict']
    output = main_processing_loop(sample_data)
    print(output)