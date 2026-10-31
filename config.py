import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth-mainnet.public.blastapi.io",
    "network_id": 1,
    "request_timeout": 15,
    "max_retries": 3,
    "gas_multiplier": 1.15,
}


@dataclass
class Config:
    rpc_url: str = DEFAULT_CONFIG["rpc_url"]
    network_id: int = DEFAULT_CONFIG["network_id"]
    request_timeout: int = DEFAULT_CONFIG["request_timeout"]
    max_retries: int = DEFAULT_CONFIG["max_retries"]
    gas_multiplier: float = DEFAULT_CONFIG["gas_multiplier"]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Config":
        valid_keys = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)


class ConfigLoader:
    def __init__(self, path: Optional[str] = None):
        self.path = path

    def load(self) -> Config:
        settings = DEFAULT_CONFIG.copy()

        if self.path and os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as file:
                file_settings = json.load(file)
                settings.update(file_settings)

        rpc_env = os.getenv("BLOCKCHAIN_RPC_URL")
        if rpc_env:
            settings["rpc_url"] = rpc_env

        net_env = os.getenv("BLOCKCHAIN_NETWORK_ID")
        if net_env and net_env.isdigit():
            settings["network_id"] = int(net_env)

        return Config.from_dict(settings)
