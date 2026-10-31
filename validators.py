import re

class AddressValidator:
    PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

    @staticmethod
    def is_ethereum_address(address: str) -> bool:
        return bool(AddressValidator.PATTERN.match(address))

class TransactionValidator:
    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def validate_gas_limit(limit: int) -> bool:
        return isinstance(limit, int) and 21000 <= limit <= 10000000

class ChainValidator:
    SUPPORTED_CHAINS = {'mainnet', 'goerli', 'sepolia'}

    @classmethod
    def is_supported(cls, chain: str) -> bool:
        return chain.lower() in cls.SUPPORTED_CHAINS