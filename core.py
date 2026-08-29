import hashlib
import json

def hash_transaction(transaction):
    tx_str = json.dumps(transaction, sort_keys=True)
    return hashlib.sha256(tx_str.encode()).hexdigest()

def generate_block_hash(previous_hash, transactions, nonce):
    block_data = previous_hash + json.dumps(transactions, sort_keys=True) + str(nonce)
    return hashlib.sha256(block_data.encode()).hexdigest()

def is_valid_hash(hash_str, difficulty):
    return hash_str.startswith('0' * difficulty)

def calculate_merkle_root(transactions):
    if not transactions:
        return ''
    hashes = [hash_transaction(tx) for tx in transactions]
    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        new_hashes = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
        hashes = new_hashes
    return hashes[0]

def validate_address(address):
    if not isinstance(address, str):
        return False
    return len(address) == 42 and address.startswith('0x')

def validate_transaction(transaction):
    required_keys = ['from', 'to', 'amount', 'nonce']
    if not all(key in transaction for key in required_keys):
        return False
    if not isinstance(transaction['amount'], (int, float)) or transaction['amount'] <= 0:
        return False
    return True