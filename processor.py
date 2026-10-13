import decimal
from typing import Dict, Any, Optional

class CryptoProcessor:
    def __init__(self, precision: int = 18):
        self.precision = precision
        decimal.getcontext().prec = precision

    def format_wei(self, value: Any) -> decimal.Decimal:
        try:
            return decimal.Decimal(str(value))
        except (decimal.InvalidOperation, ValueError):
            return decimal.Decimal(0)

    def calculate_share(self, amount: str, percentage: str) -> decimal.Decimal:
        val = self.format_wei(amount)
        ratio = self.format_wei(percentage)
        return (val * ratio / 100).quantize(decimal.Decimal(10)**-self.precision)

    def sanitize_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            k: str(v) if not isinstance(v, (int, float, dict)) else v
            for k, v in data.items()
            if v is not None
        }

def get_exchange_rate(data: Dict[str, Any], pair: str) -> Optional[decimal.Decimal]:
    rates = data.get('rates', {})
    if pair not in rates:
        return None
    return decimal.Decimal(str(rates[pair]))