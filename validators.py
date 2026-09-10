from typing import Any, Optional

class ValidationError(Exception):
    pass

def validate_address(address: Any) -> str:
    if not isinstance(address, str):
        raise ValidationError('address must be a string')
    if not (len(address) == 42 and address.startswith('0x')):
        raise ValidationError('invalid ethereum address format')
    return address

def validate_amount(amount: Any) -> float:
    try:
        val = float(amount)
        if val <= 0:
            raise ValueError
        return val
    except (TypeError, ValueError, OverflowError):
        raise ValidationError('amount must be a positive float')

def validate_chain_id(chain_id: Any) -> int:
    if not isinstance(chain_id, int) or chain_id < 0:
        raise ValidationError('chain_id must be a non-negative integer')
    return chain_id

def validate_transaction(data: dict) -> bool:
    try:
        validate_address(data.get('from'))
        validate_address(data.get('to'))
        validate_amount(data.get('value'))
        validate_chain_id(data.get('chain_id'))
        return True
    except (ValidationError, AttributeError):
        return False