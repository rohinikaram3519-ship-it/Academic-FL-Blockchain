import hashlib

data = "FedAvg Round 1"

hash_value = hashlib.sha256(
    data.encode()
).hexdigest()

print(hash_value)
