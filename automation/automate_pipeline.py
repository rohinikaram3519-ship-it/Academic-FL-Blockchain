import subprocess

subprocess.run(
    ["python", "../federated_learning/academic_dataset/generate_certificate_hash.py"]
)

subprocess.run(
    ["python", "../federated_learning/academic_dataset/generate_attestation_token.py"]
)

subprocess.run(
    ["python", "../signatures/sign_certificate_records.py"]
)

subprocess.run(
    ["python", "../blockchain/store_student_record.py"]
)

print("Pipeline Completed")