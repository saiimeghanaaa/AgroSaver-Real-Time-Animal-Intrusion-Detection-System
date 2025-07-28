import cv2
import serial
import time
from ultralytics import YOLO

# Connect to Arduino (adjust COM port as needed)
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset

# Load trained YOLO model
model = YOLO("runs/detect/train21/weights/best.pt")

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference
    results = model(frame, conf=0.3, iou=0.5)

    detected_label = None
    command = None

    # Loop through detections
    for box in results[0].boxes:
        cls = int(box.cls[0])
        class_name = model.names[cls]

        if class_name == "rat":
            detected_label = "Rat Detected!"
            color = (0, 255, 0)  # Green
            command = "rat\n"  # Send "rat" to Arduino
            break
        elif class_name == "snake":
            detected_label = "Snake Detected!"
            color = (0, 0, 255)  # Red
            command = "snake\n"  # Send "snake" to Arduino
            break

    # Send data to Arduino
    if command:
        arduino.write(command.encode())
        print(f"Sent to Arduino: {command}")

    # Display detection result
    if detected_label:
        cv2.putText(frame, detected_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("YOLOv8 Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()

