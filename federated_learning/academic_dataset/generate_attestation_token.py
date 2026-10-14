import pandas as pd
import hashlib
from datetime import datetime
import os

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "certificate_records.csv"
)

df = pd.read_csv(csv_path)

def generate_token(row):

    timestamp = str(
        datetime.now()
    )

    data = (
        str(row["student_id"])
        + row["module"]
        + row["certificate_status"]
        + timestamp
    )

    return hashlib.sha256(
        data.encode()
    ).hexdigest()

df["attestation_token"] = df.apply(
    generate_token,
    axis=1
)

df.to_csv(
    csv_path,
    index=False
)

print(
    df[
        [
            "student_id",
            "certificate_status",
            "attestation_token"
        ]
    ].head()
)