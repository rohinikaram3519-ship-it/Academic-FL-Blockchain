from ultralytics import YOLO
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

model_path = (
    project_root /
    "runs" /
    "detect" /
    "train-8" /
    "weights" /
    "best.pt"
)

model = YOLO(str(model_path))

def check_certificate(image_path):

    results = model(image_path)

    if len(results[0].boxes) > 0:

        class_id = int(
            results[0].boxes.cls[0]
        )

        class_name = model.names[class_id]

        print(
        "Detected Class:",
        class_name
    )

        return class_name.upper()

    return "UNKNOWN"