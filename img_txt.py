from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import util
from util import read_license_plate, write_csv

# Initialize results dictionary
results = {}

# Load models
coco_model = YOLO('yolov8n.pt') # yolov8 nano model
license_plate_detector = YOLO('license_plate_detector.pt') # custom model

# Load image
image_path = "2.jpg"
frame = cv2.imread(image_path)

# Detect license plates
license_plates = license_plate_detector(frame)[0]
for license_plate in license_plates.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = license_plate

    # Crop license plate
    license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

    # Process license plate
    license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
    _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

    # Read license plate number
    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

    if license_plate_text is not None:
        # Assuming a single car and license plate for simplicity
        car_id = 0
        results[0] = {
            car_id: {
                'car': {'bbox': [x1, y1, x2, y2]},
                'license_plate': {
                    'bbox': [x1, y1, x2, y2],
                    'text': license_plate_text,
                    'bbox_score': score,
                    'text_score': license_plate_text_score
                }
            }
        }

        # Print the detected license plate text
        print(f"Detected License Plate: {license_plate_text}")

        # Display the cropped license plate using matplotlib
plt.imshow(cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2RGB))
plt.title('Cropped License Plate')
plt.axis('off')  # Hide axes
plt.show()

# Write results to CSV
write_csv(results, 'test.csv')
