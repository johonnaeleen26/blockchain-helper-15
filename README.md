# blockchain-helper-15

`blockchain-helper-15` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks like contract deployment, gas estimation, and batch transaction processing for developers.

### Features

*   **Gas Oracle Integration:** Automatically fetches current network congestion data to calculate optimal gas fees for prioritized execution.
*   **Batch Transaction Executor:** Handles nonce management and bundle submission to reduce overhead when executing multiple smart contract calls.
*   **Smart Contract Wrapper:** Provides a streamlined interface for interacting with ABIs, allowing for intuitive function calls without manual encoding.
*   **Wallet Security Utilities:** Includes built-in key encryption and cold-storage signing workflows to keep sensitive credentials isolated.

### Installation

Ensure you have Python 3.9+ installed. Install the package directly via pip:

```bash
pip install blockchain-helper-15
```

For development mode, clone the repository and install requirements:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

### Usage

Here is a quick example of how to connect to a provider and fetch the latest block balance:

```python
from blockchain_helper import Client

# Initialize the client with your RPC endpoint
client = Client(rpc_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# Fetch current network stats
latest_block = client.get_latest_block_number()
gas_price = client.get_suggested_gas_price()

print(f"Current Block: {latest_block}")
print(f"Recommended Gas: {gas_price} gwei")
```

### Configuration

Set your environment variables in a `.env` file to manage private keys securely:

```text
PRIVATE_KEY=your_private_key_here
RPC_URL=your_rpc_endpoint
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.