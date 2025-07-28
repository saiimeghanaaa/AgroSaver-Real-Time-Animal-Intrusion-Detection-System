🌾 AgroSaver – Real-Time Rat & Snake Detection System
AgroSaver is a real-time animal intrusion detection system developed using deep learning, computer vision, and IoT. It aims to safeguard crops and public safety by detecting two major threats in farms and storage areas: rats and snakes. The system uses a custom-trained YOLOv8 model for detection and integrates with Arduino to trigger physical alerts via buzzer signals.

🔧 Tech Stack
YOLOv8 (Custom object detection model)

Python (Data preprocessing, model integration, OpenCV)

OpenCV (Real-time video processing)

TensorFlow + Keras (ResNet50 CNN for image classification)

Flask (API for communication, optional)

Arduino Uno (Hardware alert system)

Buzzer (1 beep for rat, 2 beeps for snake)

Virtual Serial Ports (COM5 ↔ COM6) for Python–Arduino communication

🧠 Features
✅ Custom YOLOv8 model trained on 300+ rat images and 300+ snake images

✅ Real-time detection using a webcam

✅ Arduino integration to trigger buzzer alerts

✅ Python-OpenCV pipeline for live frame capture and YOLO inference

✅ Serial communication between Python and Arduino via COM ports

✅ Animal classification using ResNet50 CNN model (as an alternative classifier)

✅ Supports real-time monitoring and data logging (optional integration with ThingSpeak or Firebase

⚙️ Workflow
Dataset Collection & Augmentation

300+ images each of rats and snakes

Augmented with rotation, flipping, brightness adjustments

Split into train/test/val sets

YOLOv8 Model Training

Annotated images using Roboflow

Trained YOLOv8 model using Ultralytics framework

Exported best weights (best.pt)

Real-Time Detection

Python + OpenCV used to capture live video frames

YOLOv8 model used to detect rats/snakes in real-time

If detected, triggers signal to Arduino

Alert System via Arduino

Python sends '1' if rat, '2' if snake via serial (COM6)

Arduino reads from COM7, activates buzzer

1 beep → rat

2 beeps → snake

(Optional) Image Classification with ResNet50

Classifier trained for additional image verification

Used if snapshot of detected frame is to be analyzed

(Optional) Logging & Notifications

Can connect to ThingSpeak for logging

Can integrate Pushover/Firebase for mobile notifications

🔌 Arduino Setup
Buzzer (trio type with S, +, –)

Connect S to Digital Pin 9, + to 5V, – to GND

Upload buzzer_alert.ino to Arduino

Ensure COM port matches Python script (e.g., COM7)
📸 Sample Output
Detected Frame	Terminal Output	Buzzer
Rat detected	Sending 1	1 beep
Snake detected	Sending 2	2 beeps

🔒 Limitations
Works best in clear lighting conditions

Only detects rats and snakes (customizable)

No GUI or Android app (console + hardware only)

Webcam required

📌 Future Scope
Add mobile notification support (Firebase)

Integrate weather data for smarter alerts

Expand dataset to include more animal types

Android app or dashboard for real-time view

👨‍💻 Author
Sai Meghana Bayya
BTech (AIML), 3rd Year
Custom YOLOv8 | Arduino Integration 
