import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "BH_") -> None:
        self.env_prefix = env_prefix
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in self.settings:
            env_var = f"{self.env_prefix}{key}"
            value = os.getenv(env_var)
            if value is not None:
                self.settings[key] = self._cast_value(value, type(self.settings[key]))

    @staticmethod
    def _cast_value(value: str, target_type: type) -> Any:
        if target_type is bool:
            return value.lower() in ("true", "1", "yes")
        return target_type(value)

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]