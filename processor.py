from typing import List, Dict, Optional

class BlockProcessor:
    """Handles processing of raw blockchain transaction data."""

    def __init__(self, network_id: str) -> None:
        self.network_id: str = network_id

    def validate_tx(self, tx: Dict[str, any]) -> bool:
        """Checks transaction schema integrity."""
        required_fields: List[str] = ["hash", "sender", "amount"]
        return all(field in tx for field in required_fields)

    def process_batch(self, transactions: List[Dict[str, any]]) -> List[str]:
        """Filters and returns list of valid transaction hashes."""
        return [tx["hash"] for tx in transactions if self.validate_tx(tx)]

    def calculate_fee(self, amount: float, rate: float = 0.001) -> float:
        """Calculates network fees based on transfer volume."""
        return round(amount * rate, 8)

def format_output(tx_data: List[str]) -> str:
    """Converts list of hashes into comma-separated string."""
    return ",".join(tx_data)