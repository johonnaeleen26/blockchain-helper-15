import re

class TransactionProcessor:
    ADDR_REGEX = re.compile("^0x[a-fA-F0-9]{40}$")
    HASH_REGEX = re.compile("^0x[a-fA-F0-9]{64}$")

    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0

    def validate_transaction(self, tx: dict) -> bool:
        if not isinstance(tx, dict):
            return False

        required_keys = {"sender", "recipient", "amount", "tx_hash"}
        if not required_keys.issubset(tx.keys()):
            return False

        if not (self.ADDR_REGEX.match(tx["sender"]) and self.ADDR_REGEX.match(tx["recipient"])):
            return False

        if not self.HASH_REGEX.match(tx["tx_hash"]):
            return False

        try:
            amount = float(tx["amount"])
            if amount <= 0:
                return False
        except (ValueError, TypeError):
            return False

        return True

    def process_batch(self, transactions: list) -> dict:
        successful_txs = []
        for tx in transactions:
            if self.validate_transaction(tx):
                successful_txs.append(tx)
                self.processed_count += 1
            else:
                self.failed_count += 1

        return {
            "processed": self.processed_count,
            "failed": self.failed_count,
            "valid_transactions": successful_txs,
        }
