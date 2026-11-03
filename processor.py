import re
from typing import Any, Dict


class ProcessingError(Exception):
    pass


class InvalidTransactionError(ProcessingError):
    pass


class InsufficientGasError(ProcessingError):
    pass


class TransactionProcessor:
    ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
    MIN_GAS_LIMIT = 21000

    def process_raw_tx(self, tx_data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(tx_data, dict):
            raise InvalidTransactionError("Payload must be a dictionary")

        required_fields = {"to", "value", "gas_limit", "gas_price", "nonce"}
        missing = required_fields - tx_data.keys()
        if missing:
            raise InvalidTransactionError(f"Missing required fields: {', '.join(sorted(missing))}")

        recipient = tx_data["to"]
        if not isinstance(recipient, str) or not self.ADDRESS_REGEX.match(recipient):
            raise InvalidTransactionError(f"Invalid Ethereum recipient address: {recipient}")

        value = tx_data["value"]
        if not isinstance(value, int) or value < 0:
            raise InvalidTransactionError("Transaction value must be a non-negative integer")

        gas_limit = tx_data["gas_limit"]
        if not isinstance(gas_limit, int) or gas_limit < self.MIN_GAS_LIMIT:
            raise InsufficientGasError(f"Gas limit must be at least {self.MIN_GAS_LIMIT}")

        gas_price = tx_data["gas_price"]
        if not isinstance(gas_price, int) or gas_price <= 0:
            raise InvalidTransactionError("Gas price must be a positive integer")

        nonce = tx_data["nonce"]
        if not isinstance(nonce, int) or nonce < 0:
            raise InvalidTransactionError("Nonce must be a non-negative integer")

        max_fee = gas_limit * gas_price
        tx_hash = f"0x{(abs(hash(f'{recipient}{nonce}{value}'))):016x}"
        return {
            "processed": True,
            "hash": tx_hash,
            "recipient": recipient.lower(),
            "value_wei": value,
            "max_fee_wei": max_fee,
            "nonce": nonce,
        }
