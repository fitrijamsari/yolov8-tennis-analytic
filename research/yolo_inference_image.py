from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

results = model.predict("../input/image_frame1.png", save=True, device="mps")

print(results[0])
print("============================================================")

for box in results[0].boxes:
    print(box)
