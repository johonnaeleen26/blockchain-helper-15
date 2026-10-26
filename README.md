# blockchain-helper-15

`blockchain-helper-15` is a lightweight Python utility designed to streamline common blockchain operations, including wallet address validation and transaction monitoring. It provides developers with a robust interface to interact with decentralized ledger data without the overhead of heavy full-node dependencies.

### Features
* **Address Validator:** Regex-based and checksum-aware validation for EVM-compatible and Bitcoin-style addresses.
* **Transaction Monitor:** Asynchronous websocket listeners to track pending transactions or specific address activity in real-time.
* **Unit Converter:** Built-in utilities for seamless Wei to Ether (and vice versa) conversions with high-precision decimal support.
* **Gas Estimator:** Integrated logic to fetch current gas prices and calculate optimal transaction fees based on network congestion.

### Installation

Ensure you have Python 3.8+ installed. You can install the package via pip:

```bash
pip install blockchain-helper-15
```

For development mode, clone the repository and install the requirements:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

### Basic Usage

```python
from blockchain_helper import AddressValidator, GasEstimator

# Validate an address
validator = AddressValidator(network='ethereum')
is_valid = validator.is_valid("0x71C7656EC7ab88b098defB751B7401B5f6d8976F")
print(f"Address valid: {is_valid}")

# Estimate gas for a standard transfer
estimator = GasEstimator(rpc_url="https://cloudflare-eth.com")
fee = estimator.get_current_gas_price()
print(f"Current gas price: {fee} Gwei")
```

### License
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.