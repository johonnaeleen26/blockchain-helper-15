from typing import Any, Dict


def validate_transaction_payload(payload: Dict[str, Any]) -> None:
    required_fields = {'sender', 'recipient', 'amount', 'signature'}
    if not all(field in payload for field in required_fields):
        raise ValueError('missing mandatory transaction fields')

    if not isinstance(payload['amount'], (int, float)) or payload['amount'] <= 0:
        raise ValueError('invalid transaction amount')

    if not isinstance(payload['signature'], str) or len(payload['signature']) < 64:
        raise ValueError('invalid cryptographic signature length')


def validate_block_hash(block_hash: str) -> bool:
    if not isinstance(block_hash, str) or len(block_hash) != 64:
        return False
    return all(c in '0123456789abcdef' for c in block_hash.lower())


def sanitize_address(address: str) -> str:
    clean_address = address.strip().lower()
    if not clean_address.startswith('0x') or len(clean_address) != 42:
        raise ValueError('malformed blockchain address format')
    return clean_address