from web3 import Web3
from solcx import compile_source
import hashlib

# Connect Ganache
w3 = Web3(
    Web3.HTTPProvider(
        "http://127.0.0.1:8545"
    )
)

# Load contract
with open(
    "contracts/ModelRegistry.sol",
    "r"
) as f:
    source = f.read()

compiled_sol = compile_source(
    source,
    output_values=["abi", "bin"],
    solc_version="0.8.20"
)

contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]

print("Connected:", w3.is_connected())

# Replace this with your deployed address
contract_address = Web3.to_checksum_address(
"0x1bfC23e06e264d74487206D628D5ce586e7e6d7b"
)

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

account = w3.eth.accounts[0]

# Example FedAvg Hash

data = "FedAvg Round 1"

model_hash = "a7c1c552cf12218404314d5b920fb467eafb86c47a635ecfce9c833ed7bfd71a"

tx_hash = contract.functions.addModel(
    1,
    model_hash,
    80
).transact(
    {
        "from": account
    }
)

receipt = w3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("Address:", contract_address)

print("Stored Successfully")

print("Transaction Hash:")

print(
    tx_hash.hex()
)