import json
import os
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional


@dataclass
class Config:
    rpc_url: str = "https://mainnet.infura.io/v3/default"
    chain_id: int = 1
    request_timeout: int = 30
    max_retries: int = 3
    gas_limit_default: int = 21000
    confirmation_blocks: int = 2

    @classmethod
    from_dict(cls, data: Dict[str, Any]) -> "Config":
        valid_keys = {field for field in cls.__dataclass_fields__}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)

    @classmethod
    def load_from_file(cls, filepath: Optional[str] = None) -> "Config":
        if not filepath or not os.path.exists(filepath):
            return cls()
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)

    @classmethod
    def load_from_env(cls) -> "Config":
        env_mappings = {
            "RPC_URL": ("rpc_url", str),
            "CHAIN_ID": ("chain_id", int),
            "REQUEST_TIMEOUT": ("request_timeout", int),
            "MAX_RETRIES": ("max_retries", int),
            "GAS_LIMIT_DEFAULT": ("gas_limit_default", int),
            "CONFIRMATION_BLOCKS": ("confirmation_blocks", int),
        }
        data = {}
        for env_key, (config_key, target_type) in env_mappings.items():
            val = os.getenv(env_key)
            if val is not None:
                data[config_key] = target_type(val)
        return cls.from_dict(data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
