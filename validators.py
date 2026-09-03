import re


class BlockchainValidationError(ValueError):
    pass


class InvalidAddressError(BlockchainValidationError):
    pass


class InvalidTxHashError(BlockchainValidationError):
    pass


class InvalidGasLimitError(BlockchainValidationError):
    pass


EVM_ADDRESS_REGEX = re.compile(r'^0x[a-fA-F0-9]{40}$')
TX_HASH_REGEX = re.compile(r'^0x[a-fA-F0-9]{64}$')


def validate_evm_address(address: str) -> str:
    if not isinstance(address, str):
        raise InvalidAddressError('Address must be a string')
    clean_address = address.strip()
    if not EVM_ADDRESS_REGEX.match(clean_address):
        raise InvalidAddressError(f'Invalid EVM address format: {clean_address}')
    return clean_address


def validate_tx_hash(tx_hash: str) -> str:
    if not isinstance(tx_hash, str):
        raise InvalidTxHashError('Transaction hash must be a string')
    clean_hash = tx_hash.strip()
    if not TX_HASH_REGEX.match(clean_hash):
        raise InvalidTxHashError(f'Invalid transaction hash format: {clean_hash}')
    return clean_hash


def validate_gas_limit(gas_limit: int, minimum: int = 21000) -> int:
    if not isinstance(gas_limit, int) or isinstance(gas_limit, bool):
        raise InvalidGasLimitError('Gas limit must be an integer')
    if gas_limit < minimum:
        raise InvalidGasLimitError(f'Gas limit {gas_limit} below minimum {minimum}')
    return gas_limit
