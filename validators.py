import re


def validate_address(address: str) -> bool:
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))


def validate_transaction_hash(tx_hash: str) -> bool:
    pattern = r'^0x[a-fA-F0-9]{64}$'
    return bool(re.match(pattern, tx_hash))


def validate_uint256(value: str) -> bool:
    try:
        val = int(value)
        return 0 <= val <= 2**256 - 1
    except ValueError:
        return False


def validate_chain_id(chain_id: int) -> bool:
    return isinstance(chain_id, int) and chain_id > 0


def validate_gas_price(gas_price: int) -> bool:
    return isinstance(gas_price, int) and gas_price >= 0


def sanitize_input(data: str) -> str:
    return data.strip().lower()
