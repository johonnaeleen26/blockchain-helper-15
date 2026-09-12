from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional


class CryptoProcessor:
    def __init__(self, precision: int = 8):
        self.precision = precision

    def format_amount(self, value: float) -> Decimal:
        return Decimal(str(value)).quantize(
            Decimal(10) ** -self.precision, 
            rounding=ROUND_HALF_UP
        )

    def calculate_trade_volume(self, prices: List[float], quantities: List[float]) -> Decimal:
        if len(prices) != len(quantities):
            raise ValueError("mismatched data list lengths")
        
        total = sum(Decimal(str(p)) * Decimal(str(q)) for p, q in zip(prices, quantities))
        return total.quantize(Decimal('1.00000000'))

    def filter_dust(self, data: Dict[str, float], threshold: float = 0.0001) -> Dict[str, float]:
        return {k: v for k, v in data.items() if v >= threshold}

    def aggregate_balances(self, assets: List[Dict[str, float]]) -> Dict[str, Decimal]:
        totals: Dict[str, Decimal] = {}
        for asset in assets:
            for coin, amount in asset.items():
                totals[coin] = totals.get(coin, Decimal('0')) + Decimal(str(amount))
        return {k: v.quantize(Decimal('1.00000000')) for k, v in totals.items()}