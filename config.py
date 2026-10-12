import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "chain_id": 1
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
    return config

class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self._data = load_config(path)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    @property
    def rpc_url(self) -> str:
        return self._data.get("rpc_url", DEFAULT_CONFIG["rpc_url"])

    @property
    def timeout(self) -> int:
        return int(self._data.get("timeout", DEFAULT_CONFIG["timeout"]))

    @property
    def chain_id(self) -> int:
        return int(self._data.get("chain_id", DEFAULT_CONFIG["chain_id"]))
