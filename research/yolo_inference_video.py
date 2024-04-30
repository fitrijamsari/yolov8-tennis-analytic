import torch
from ultralytics import YOLO

print(torch.backends.mps.is_available())

# Load a model
model = YOLO("yolov8n.pt")

video_path = "../input/tennis_video.mp4"

# results = model.predict(source=video_path, show=True, conf=0.1, save=True, device="mps")
results = model.track(source=video_path, show=True, conf=0.1, save=True, device="mps")
