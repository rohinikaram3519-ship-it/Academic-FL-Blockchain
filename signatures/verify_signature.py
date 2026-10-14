import pandas as pd
from ecdsa import VerifyingKey

with open(
    "public_key.pem",
    "rb"
) as f:

    public_key = VerifyingKey.from_pem(
        f.read()
    )

df = pd.read_csv(
    "../federated_learning/academic_dataset/data/certificate_records.csv"
)

row = df.iloc[0]

message = (
    str(row["student_id"])
    + "|"
    + row["module"]
    + "|"
    + row["certificate_status"]
)

signature = bytes.fromhex(
    row["signature"]
)

valid = public_key.verify(
    signature,
    message.encode()
)

print(
    "Signature Valid:",
    valid
)