from ultralytics import YOLO

# Load and train the model
model = YOLO("yolov8n.yaml")
results = model.train(data="config.yaml", epochs=140)

# Convert to TFLite
model.export(format="tflite")
