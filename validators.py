from typing import Any, Dict

class ValidationError(Exception):
    pass

def validate_transaction_schema(data: Dict[str, Any]) -> None:
    required = {'sender', 'receiver', 'amount', 'signature'}
    if not isinstance(data, dict):
        raise ValidationError('payload must be a dictionary')
    if not required.issubset(data.keys()):
        raise ValidationError(f'missing required fields: {required - data.keys()}')
    if not isinstance(data.get('amount'), (int, float)) or data['amount'] <= 0:
        raise ValidationError('invalid transaction amount')
    if not isinstance(data.get('signature'), str) or len(data['signature']) < 64:
        raise ValidationError('invalid signature format')

def validate_network_node(url: str) -> None:
    if not url.startswith(('http://', 'https://')):
        raise ValidationError('invalid node url scheme')
    if len(url) < 10:
        raise ValidationError('node url too short')

def validate_block_height(height: int) -> None:
    if not isinstance(height, int) or height < 0:
        raise ValidationError('block height must be non-negative integer')
