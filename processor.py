import re
from typing import Any, Dict, List


class InvalidPayloadError(Exception):
    pass


class TransactionProcessor:
    HEX_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
    HEX_HASH_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")

    def __init__(self, supported_chain_ids: List[int]) -> None:
        self.supported_chain_ids = set(supported_chain_ids)

    def validate_tx_payload(self, tx: Dict[str, Any]) -> None:
        if not isinstance(tx, dict):
            raise InvalidPayloadError("Payload must be a dictionary")

        required_fields = {"sender", "recipient", "amount", "chain_id", "tx_hash"}
        missing = required_fields - tx.keys()
        if missing:
            raise InvalidPayloadError(f"Missing required fields: {', '.join(missing)}")

        if not self.HEX_ADDRESS_REGEX.match(str(tx.get("sender", ""))):
            raise InvalidPayloadError("Invalid sender address format")

        if not self.HEX_ADDRESS_REGEX.match(str(tx.get("recipient", ""))):
            raise InvalidPayloadError("Invalid recipient address format")

        if not self.HEX_HASH_REGEX.match(str(tx.get("tx_hash", ""))):
            raise InvalidPayloadError("Invalid transaction hash format")

        amount = tx.get("amount")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidPayloadError("Amount must be a positive number")

        chain_id = tx.get("chain_id")
        if chain_id not in self.supported_chain_ids:
            raise InvalidPayloadError(f"Unsupported chain ID: {chain_id}")

    def process_batch(self, payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for payload in payloads:
            try:
                self.validate_tx_payload(payload)
                processed.append({
                    "tx_hash": payload["tx_hash"],
                    "status": "valid",
                    "sender": payload["sender"].lower(),
                    "recipient": payload["recipient"].lower(),
                    "amount": float(payload["amount"]),
                    "chain_id": payload["chain_id"],
                })
            except InvalidPayloadError as exc:
                processed.append({
                    "tx_hash": payload.get("tx_hash"),
                    "status": "rejected",
                    "reason": str(exc),
                })
        return processed
