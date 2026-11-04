import re

class ValidationError(Exception):
    pass

def validate_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str) or not re.fullmatch(r'0x[a-fA-F0-9]{64}', tx_hash):
        raise ValidationError(f"Invalid transaction hash format: {tx_hash}")
    return True

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or not re.fullmatch(r'0x[a-fA-F0-9]{40}', address):
        raise ValidationError(f"Invalid address format: {address}")
    return True

def process_transactions(queue: list):
    for item in queue:
        try:
            tx_hash = item.get("hash")
            address = item.get("address")
            
            validate_tx_hash(tx_hash)
            validate_address(address)
            
            print(f"Processing {tx_hash} for {address}")
        except (ValidationError, AttributeError) as e:
            print(f"Skipping invalid entry: {e}")
            continue