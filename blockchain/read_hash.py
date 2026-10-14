from web3 import Web3
from solcx import compile_source

w3 = Web3(
    Web3.HTTPProvider(
        "http://127.0.0.1:8545"
    )
)

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


contract_address = Web3.to_checksum_address(
    "0x1bfC23e06e264d74487206D628D5ce586e7e6d7b"
)

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

print("Connected:", w3.is_connected())
print("Address:", contract_address)
print("Code size:", len(w3.eth.get_code(contract_address)))


record = contract.functions.getModel(
    0
).call()

print(record)