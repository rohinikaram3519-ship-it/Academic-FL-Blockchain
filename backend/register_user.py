from web3 import Web3
import json

def create_identity(
    student_id,
    student_name,
    password
):

    account = Web3().eth.account.create()

    wallet_address = account.address

    node_id = f"NODE_{student_id}"

    try:

        with open(
            "users.json",
            "r"
        ) as f:

            users = json.load(f)

    except FileNotFoundError:

        users = []

    users.append({

        "username":
        str(student_id),

        "password":
        password,

        "studentName":
        student_name

    })

    with open(
        "users.json",
        "w"
    ) as f:

        json.dump(
            users,
            f,
            indent=4
        )

    print(
        "Student ID:",
        student_id
    )

    return {

        "nodeId":
        node_id,

        "walletAddress":
        wallet_address

    }