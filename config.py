import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional


DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.2,
    "cache_dir": "~/.cache/blockchain-helper",
}


@dataclass
class Config:
    network: str = DEFAULT_CONFIG["network"]
    rpc_url: str = DEFAULT_CONFIG["rpc_url"]
    timeout: int = DEFAULT_CONFIG["timeout"]
    max_retries: int = DEFAULT_CONFIG["max_retries"]
    gas_limit_multiplier: float = DEFAULT_CONFIG["gas_limit_multiplier"]
    cache_dir: str = DEFAULT_CONFIG["cache_dir"]

    def __post_init__(self) -> None:
        self.cache_dir = os.path.expanduser(self.cache_dir)


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = Path(config_path) if config_path else None

    def load(self) -> Config:
        data = DEFAULT_CONFIG.copy()

        if self.config_path and self.config_path.is_file():
            with open(self.config_path, "r", encoding="utf-8") as f:
                data.update(json.load(f))

        env_rpc = os.getenv("BLOCKCHAIN_RPC_URL")
        if env_rpc:
            data["rpc_url"] = env_rpc

        env_network = os.getenv("BLOCKCHAIN_NETWORK")
        if env_network:
            data["network"] = env_network

        valid_keys = Config.__annotations__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return Config(**filtered_data)
