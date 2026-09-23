# blockchain-helper-15

`blockchain-helper-15` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks like contract event monitoring, gas estimation, and batch transaction processing.

## Features

*   **Automated Gas Oracle:** Fetch real-time gas prices and estimate network fees with configurable priority levels to ensure timely transaction inclusion.
*   **Event Stream Listener:** Robust, asynchronous listeners that capture and parse blockchain logs, providing seamless integration with off-chain notification systems.
*   **Batch Processor:** Execute bulk transfers or contract interactions in a single transaction batch to minimize gas overhead and reduce latency.
*   **Secure Wallet Manager:** Simplifies keystore management and private key handling using industry-standard encryption protocols.

## Installation

Ensure you have Python 3.9+ installed. Install the package directly via pip:

```bash
pip install blockchain-helper-15
```

For local development and dependency management:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

## Basic Usage

The following example demonstrates how to initialize the helper and retrieve the current network base fee:

```python
from blockchain_helper import Client

# Initialize the client with an RPC provider
client = Client(rpc_url="https://eth-mainnet.public.blastapi.io")

# Fetch current gas fees
gas_stats = client.get_gas_metrics()
print(f"Standard Gas Price: {gas_stats['standard']} Gwei")

# Listen for a specific event
client.watch_contract_event(
    address="0x123...abc",
    event_name="Transfer",
    callback=lambda log: print(f"New transfer detected: {log}")
)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.