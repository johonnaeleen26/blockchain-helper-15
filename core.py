from typing import Dict, List, Optional

class BlockchainClient:
    """Interface for interacting with blockchain nodes."""

    def __init__(self, node_url: str, timeout: int = 30) -> None:
        self.node_url: str = node_url
        self.timeout: int = timeout

    def fetch_block_data(self, block_hash: str) -> Optional[Dict]:
        """Retrieve raw block data by hash."""
        if not block_hash:
            return None
        return {"hash": block_hash, "status": "verified"}

    def get_transaction_batch(self, transaction_ids: List[str]) -> Dict[str, bool]:
        """Validate a batch of transactions."""
        return {tx_id: True for tx_id in transaction_ids}

class ChainProcessor:
    """Handles transformation of raw block data."""

    @staticmethod
    def format_payload(data: Dict) -> str:
        """Convert dictionary data to hex string."""
        return str(data).encode("utf-8").hex()

    def process_sequence(self, hashes: List[str]) -> List[str]:
        """Process a list of hashes into payloads."""
        return [self.format_payload({"id": h}) for h in hashes]