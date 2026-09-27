from typing import Dict, List, Any
from decimal import Decimal, ROUND_HALF_UP

class CryptoProcessor:
    @staticmethod
    def format_balance(amount: str, precision: int = 8) -> Decimal:
        return Decimal(amount).quantize(
            Decimal('1.' + '0' * precision),
            rounding=ROUND_HALF_UP
        )

    @staticmethod
    def calculate_trade_value(price: str, quantity: str) -> Decimal:
        return Decimal(price) * Decimal(quantity)

    @staticmethod
    def normalize_ticker(ticker: str) -> str:
        return ticker.strip().upper().replace('/', '_')

    def batch_process_rates(data: List[Dict[str, Any]]) -> Dict[str, Decimal]:
        results = {}
        for entry in data:
            ticker = self.normalize_ticker(entry.get('symbol', ''))
            rate = entry.get('price', '0')
            results[ticker] = Decimal(rate)
        return results