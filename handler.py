from typing import List, Dict, Optional

class BlockchainHandler:
    def __init__(self, network: str = 'mainnet') -> None:
        self.network: str = network

    def format_transaction(self, tx_id: str, amount: float) -> Dict[str, str]:
        """Format transaction data for blockchain broadcast."""
        return {
            "id": tx_id,
            "amount": f"{amount:.8f}",
            "network": self.network
        }

    def validate_batch(self, transactions: List[Dict[str, str]]) -> bool:
        """Check if all transactions contain required fields."""
        required = {"id", "amount", "network"}
        return all(required.issubset(tx.keys()) for tx in transactions)

    def process_sequence(self, ids: List[str]) -> Optional[List[str]]:
        """Verify and return transaction identifier sequence."""
        if not ids:
            return None
        return [f"processed_{i}" for i in ids]