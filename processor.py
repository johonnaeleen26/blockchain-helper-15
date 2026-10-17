from typing import List, Dict, Optional

class TransactionProcessor:
    """Handles validation and processing of blockchain transactions."""

    def __init__(self, chain_id: int) -> None:
        self.chain_id: int = chain_id
        self.processed_count: int = 0

    def validate(self, tx_data: Dict[str, str]) -> bool:
        """Validates the integrity of transaction data."""
        required_fields: List[str] = ['sender', 'recipient', 'amount']
        return all(field in tx_data for field in required_fields)

    def process_batch(self, transactions: List[Dict[str, str]]) -> Dict[str, int]:
        """Processes a list of transactions and returns status counts."""
        results: Dict[str, int] = {'success': 0, 'failed': 0}

        for tx in transactions:
            if self.validate(tx):
                self.processed_count += 1
                results['success'] += 1
            else:
                results['failed'] += 1
        
        return results

    def get_status(self) -> Optional[str]:
        """Returns the current processor status message."""
        if self.processed_count == 0:
            return None
        return f"chain_{self.chain_id}_processed_{self.processed_count}"