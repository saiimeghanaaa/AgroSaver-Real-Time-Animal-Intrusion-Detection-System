from ultralytics import YOLO

#Load a model
model = YOLO("yolov8n.yaml") #build a new model from scratch

#use the model
results = model.train(data="config.yaml", epochs=125) #train the model