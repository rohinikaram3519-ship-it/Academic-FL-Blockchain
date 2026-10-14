from web3 import Web3
import json

# Connect Blockchain

w3 = Web3(
    Web3.HTTPProvider(
        "http://127.0.0.1:8545"
    )
)

contract_address = (
    "0x0Fc5c29480f4E5894dA7e23678c5eB10Ff38E773"
)

# Load ABI

with open(
    "../blockchain/build/contracts/AcademicVerification.json",
    "r"
) as f:

    contract_json = json.load(f)

abi = contract_json["abi"]

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

# Ask User

student_id = int(
    input(
        "Enter Student ID: "
    )
)

# Check First Blockchain Record

record = contract.functions.getRecord(
    0
).call()

# Verify

if record[0] == student_id:

    print("\n✅ CERTIFICATE VERIFIED")

    print("\nStudent ID:", record[0])

    print("Module:", record[1])

    print("Status:", record[2])

    print(
        "Verification Hash:",
        record[3]
    )

    print(
        "Attestation Token:",
        record[4]
    )

else:

    print(
        "\n CERTIFICATE NOT FOUND"
    )