import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retries": 3,
    "debug": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def get_env_overrides(config: Dict[str, Any]) -> Dict[str, Any]:
    for key in config:
        env_val = os.getenv(f"BLOCKCHAIN_{key.upper()}")
        if env_val is not None:
            try:
                config[key] = type(config[key])(env_val)
            except (ValueError, TypeError):
                pass
    return config