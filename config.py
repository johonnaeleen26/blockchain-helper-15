import json
import os
from typing import Any, Dict, Optional

DEFAULTS: Dict[str, Any] = {
    "network": "mainnet",
    "api_endpoint": "https://api.example.com",
    "timeout": 30,
    "max_retries": 3,
    "gas_price": 20,
    "blockchain_type": "ethereum",
}

class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config: Dict[str, Any] = DEFAULTS.copy()
        if config_path:
            self.load_from_file(config_path)
        self.load_from_environment()

    def load_from_file(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                file_config: Dict[str, Any] = json.load(f)
                self.config.update(file_config)

    def load_from_environment(self) -> None:
        prefix = "BLOCKCHAIN_"
        for key in list(self.config.keys()):
            env_key = prefix + key.upper()
            if env_key in os.environ:
                value = os.environ[env_key]
                original = self.config[key]
                if isinstance(original, int):
                    try:
                        self.config[key] = int(value)
                    except ValueError:
                        self.config[key] = value
                elif isinstance(original, float):
                    try:
                        self.config[key] = float(value)
                    except ValueError:
                        self.config[key] = value
                else:
                    self.config[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def save_to_file(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def __repr__(self) -> str:
        return f"ConfigLoader({self.config})"