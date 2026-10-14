from ecdsa import SigningKey

message = (
    "11391|AAA|Eligible"
)

with open(
    "private_key.pem",
    "rb"
) as f:

    private_key = SigningKey.from_pem(
        f.read()
    )

signature = private_key.sign(
    message.encode()
)

print(
    signature.hex()
)