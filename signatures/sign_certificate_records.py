import pandas as pd
from ecdsa import SigningKey

# Load private key

import os

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(
        BASE_DIR,
        "private_key.pem"
    ),
    "rb"
) as f:

    private_key = SigningKey.from_pem(
        f.read()
    )

# Load certificate records

df = pd.read_csv(
    "../federated_learning/academic_dataset/data/certificate_records.csv"
)

# Generate signature

def generate_signature(row):

    message = (

        str(row["student_id"])
        + "|"

        + str(row["module"])
        + "|"

        + str(row["certificate_status"])

    )

    signature = private_key.sign(
        message.encode()
    )

    return signature.hex()

# Add new column

df["signature"] = df.apply(
    generate_signature,
    axis=1
)

# Save

df.to_csv(
    "../federated_learning/academic_dataset/data/certificate_records.csv",
    index=False
)

print(
    df[
        [
            "student_id",
            "signature"
        ]
    ].head()
)