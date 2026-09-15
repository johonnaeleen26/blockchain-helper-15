import re

class InputValidator:
    ADDRESS_REGEX = re.compile(r'^0x[a-fA-F0-9]{40}$')
    TX_HASH_REGEX = re.compile(r'^0x[a-fA-F0-9]{64}$')

    @staticmethod
    def validate_address(address: str) -> bool:
        return bool(InputValidator.ADDRESS_REGEX.match(address))

    @staticmethod
    def validate_tx_hash(tx_hash: str) -> bool:
        return bool(InputValidator.TX_HASH_REGEX.match(tx_hash))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

def validate_payload(payload: dict) -> bool:
    if not InputValidator.validate_address(payload.get('address', '')):
        return False
    if not InputValidator.validate_amount(payload.get('amount', 0)):
        return False
    return True