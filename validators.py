import re

class BlockchainValidator:
    ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
    TX_HASH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{64}$')

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(BlockchainValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def validate_tx_hash(tx_hash: str) -> bool:
        return bool(BlockchainValidator.TX_HASH_PATTERN.match(tx_hash))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

def process_input(data: dict) -> bool:
    required_fields = ['address', 'tx_hash', 'amount']
    if not all(field in data for field in required_fields):
        return False
    
    if not BlockchainValidator.validate_address(data['address']):
        return False
    if not BlockchainValidator.validate_tx_hash(data['tx_hash']):
        return False
    if not BlockchainValidator.validate_amount(data['amount']):
        return False
        
    return True