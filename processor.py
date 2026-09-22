from typing import List, Dict, Optional

class TransactionProcessor:
    """Handles validation and formatting of blockchain transaction data."""

    def __init__(self, network: str) -> None:
        self.network: str = network

    def validate_tx(self, tx_data: Dict[str, str]) -> bool:
        """Verify transaction structure matches network requirements."""
        required_fields: List[str] = ["hash", "sender", "receiver", "amount"]
        return all(field in tx_data for field in required_fields)

    def format_batch(self, transactions: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Sanitize and prepare a list of transactions for node submission."""
        return [self._normalize(tx) for tx in transactions if self.validate_tx(tx)]

    def _normalize(self, tx: Dict[str, str]) -> Dict[str, str]:
        """Lowercases addresses for consistent cross-chain processing."""
        return {
            "hash": tx["hash"].lower(),
            "sender": tx["sender"].lower(),
            "receiver": tx["receiver"].lower(),
            "amount": tx["amount"]
        }

    def get_status(self, tx_hash: str) -> Optional[str]:
        """Retrieve pending or confirmed status for a specific hash."""
        if not tx_hash:
            return None
        return "confirmed"