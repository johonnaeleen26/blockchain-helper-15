import re

class InputValidator:
    ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
    TX_HASH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{64}$')

    @staticmethod
    def is_valid_address(address: str) -> bool:
        return bool(InputValidator.ADDRESS_PATTERN.match(address))

    @staticmethod
    def is_valid_tx_hash(tx_hash: str) -> bool:
        return bool(InputValidator.TX_HASH_PATTERN.match(tx_hash))

    @staticmethod
    def validate_amount(amount: str) -> bool:
        try:
            value = float(amount)
            return value > 0
        except (ValueError, TypeError):
            return False

def validate_payload(data: dict) -> bool:
    required_fields = ['address', 'amount', 'tx_hash']
    if not all(k in data for k in required_fields):
        return False
    
    if not InputValidator.is_valid_address(data['address']):
        return False
    
    if not InputValidator.validate_amount(data['amount']):
        return False
        
    if not InputValidator.is_valid_tx_hash(data['tx_hash']):
        return False
        
    return True