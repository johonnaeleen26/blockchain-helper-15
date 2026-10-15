# blockchain-helper-15

`blockchain-helper-15` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks such as address validation, transaction gas estimation, and real-time event monitoring for decentralized applications.

## Features

*   **Gas Oracle Integration:** Automatically fetches current network gas prices and suggests optimal priority fees based on real-time mempool congestion.
*   **Smart Contract Interaction:** Provides a streamlined wrapper for Web3.py to deploy, interact with, and verify contracts with minimal boilerplate.
*   **Event Watcher:** Built-in asynchronous listener for filtering and processing specific contract logs or transfer events in real-time.
*   **Balance Aggregator:** Batch-query utility to retrieve ERC-20 token balances for multiple addresses in a single RPC call, significantly reducing latency.

## Installation

Ensure you have Python 3.9+ installed. You can install the package via pip:

```bash
pip install blockchain-helper-15
```

For development purposes, clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

## Usage

Below is a quick example of how to connect to a provider and retrieve the gas price:

```python
from blockchain_helper import Client

# Initialize with your RPC provider
client = Client(rpc_url="https://mainnet.infura.io/v3/YOUR_API_KEY")

# Get recommended gas price in Gwei
gas_price = client.get_gas_price()
print(f"Current recommended gas price: {gas_price} Gwei")

# Validate an Ethereum address
is_valid = client.is_address("0x71C7656EC7ab88b098defB751B7401B5f6d8976F")
print(f"Address valid: {is_valid}")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.