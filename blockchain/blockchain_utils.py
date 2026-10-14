import hashlib

def generate_model_hash(data):

    return hashlib.sha256(
        data.encode()
    ).hexdigest()

print(
    generate_model_hash(
        "fedavg_model"
    )
)