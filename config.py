import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "BLOCK_TIME_SECONDS": 12,
}

def load_config(env_vars: Dict[str, str] = None) -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    env = env_vars or os.environ
    
    for key in config.keys():
        value = env.get(key)
        if value:
            if isinstance(config[key], int):
                config[key] = int(value)
            else:
                config[key] = value
    
    return config

if __name__ == "__main__":
    cfg = load_config()
    print(cfg)