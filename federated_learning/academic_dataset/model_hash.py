import hashlib

with open("final_model.pt", "rb") as f:
    model_data = f.read()

model_hash = hashlib.sha256(model_data).hexdigest()

print("Model Hash:")
print(model_hash)