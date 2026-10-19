import re
from typing import Any


class BlockchainValidator:
    ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
    BTC_ADDRESS_PATTERN = re.compile(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$")
    TX_HASH_PATTERN = re.compile(r"^(0x)?[a-fA-F0-9]{64}$")

    @classmethod
    def is_valid_eth_address(cls, address: str) -> bool:
        if not isinstance(address, str):
            return False
        return bool(cls.ETH_ADDRESS_PATTERN.match(address))

    @classmethod
    def is_valid_btc_address(cls, address: str) -> bool:
        if not isinstance(address, str):
            return False
        return bool(cls.BTC_ADDRESS_PATTERN.match(address))

    @classmethod
    def is_valid_tx_hash(cls, tx_hash: str) -> bool:
        if not isinstance(tx_hash, str):
            return False
        return bool(cls.TX_HASH_PATTERN.match(tx_hash))

    @staticmethod
    def is_valid_amount(value: Any) -> bool:
        try:
            amount = float(value)
            return amount > 0 and not isinstance(value, bool)
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_payload(data: dict) -> bool:
        required_keys = {"sender", "recipient", "amount"}
        if not isinstance(data, dict):
            return False
        return required_keys.issubset(data.keys())
