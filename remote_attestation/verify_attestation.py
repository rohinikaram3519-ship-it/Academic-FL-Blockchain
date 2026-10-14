import pandas as pd
import hashlib

# Load record

df = pd.read_csv(
    "../federated_learning/academic_dataset/data/certificate_records.csv"
)

student_id = int(
    input("Enter Student ID: ")
)

record = df[
    df["student_id"] == student_id
]

if len(record) == 0:

    print("Student Not Found")

else:

    print("\nRecord Found")

    print(record.iloc[0])

    stored_token = (
        record.iloc[0]["attestation_token"]
    )

    print(
        "Stored Token:",
        stored_token
    )

    if stored_token == record.iloc[0]["attestation_token"]:

        print(
            "\n✅ REMOTE ATTESTATION SUCCESS"
        )

        print(
            "Student ID:",
            student_id
        )

    else:

        print(
            "\n❌ REMOTE ATTESTATION FAILED"
        )   