from ultralytics import YOLO
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

dataset_yaml = (
    project_root /
    "datasets" /
    "certificate_forgery" /
    "data.yaml"
)

print("Dataset Path:", dataset_yaml)

model = YOLO("yolov8n.pt")

model.train(
    data=str(dataset_yaml),
    epochs=25,
    imgsz=640
)