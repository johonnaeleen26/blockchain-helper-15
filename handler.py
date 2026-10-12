import hashlib
import json
from decimal import Decimal
from typing import Any, Dict


class CryptoDataHandler:
    WEI_PER_ETHER = Decimal("1000000000000000000")

    @classmethod
    def wei_to_ether(cls, wei_value: int) -> Decimal:
        if wei_value < 0:
            raise ValueError("Wei value cannot be negative")
        return Decimal(wei_value) / cls.WEI_PER_ETHER

    @classmethod
    def ether_to_wei(cls, ether_value: Decimal) -> int:
        if ether_value < 0:
            raise ValueError("Ether value cannot be negative")
        return int(ether_value * cls.WEI_PER_ETHER)

    @staticmethod
    def parse_raw_transaction(raw_tx: Dict[str, Any]) -> Dict[str, Any]:
        required_keys = {"from", "to", "value", "nonce"}
        if not required_keys.issubset(raw_tx.keys()):
            missing = required_keys - raw_tx.keys()
            raise KeyError(f"Missing required keys: {missing}")

        value_int = int(raw_tx["value"])
        return {
            "sender": str(raw_tx["from"]).lower(),
            "recipient": str(raw_tx["to"]).lower(),
            "value_wei": value_int,
            "value_ether": float(CryptoDataHandler.wei_to_ether(value_int)),
            "nonce": int(raw_tx["nonce"]),
        }

    @staticmethod
    def compute_payload_hash(payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()
