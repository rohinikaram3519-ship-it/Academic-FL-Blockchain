from ecdsa import SigningKey, NIST256p

private_key = SigningKey.generate(
    curve=NIST256p
)

public_key = private_key.verifying_key

with open(
    "private_key.pem",
    "wb"
) as f:

    f.write(
        private_key.to_pem()
    )

with open(
    "public_key.pem",
    "wb"
) as f:

    f.write(
        public_key.to_pem()
    )

print("Keys Generated")