import re
from typing import Any, Dict, List

ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
TX_HASH_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")


class InvalidPayloadError(Exception):
    pass


def validate_payload(data: Dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise InvalidPayloadError("Payload must be a dictionary")

    sender = data.get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")
    tx_hash = data.get("tx_hash")

    if not sender or not ADDRESS_REGEX.match(str(sender)):
        raise InvalidPayloadError(f"Invalid sender address: {sender}")

    if not recipient or not ADDRESS_REGEX.match(str(recipient)):
        raise InvalidPayloadError(f"Invalid recipient address: {recipient}")

    if not isinstance(amount, (int, float)) or amount <= 0:
        raise InvalidPayloadError(f"Invalid transaction amount: {amount}")

    if tx_hash and not TX_HASH_REGEX.match(str(tx_hash)):
        raise InvalidPayloadError(f"Invalid transaction hash: {tx_hash}")


def process_transaction_queue(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for item in items:
        try:
            validate_payload(item)
            results.append({
                "tx_hash": item.get("tx_hash"),
                "status": "validated",
                "amount": item["amount"]
            })
        except InvalidPayloadError as err:
            results.append({
                "status": "rejected",
                "reason": str(err)
            })
    return results
