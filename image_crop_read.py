'''from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import cv2
import easyocr
import util
from util import read_license_plate, write_csv
def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to use

    # Perform text extraction
    results = reader.readtext(image)

    # Combine the results into a single string
    extracted_text = ' '.join([result[1] for result in results])

    return extracted_text
# Initialize results dictionary
results = {}

# Load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('license_plate_detector.pt')

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
plt.imshow(cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2RGB))
plt.title('Cropped License Plate')
plt.axis('off')  # Hide axes
plt.show()
image_path = 'path_to_your_image.jpg'
text = extract_text_from_image(image_path)
print(text)
'''
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import cv2
import easyocr

def extract_text_from_image(image):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to use

    # Perform text extraction
    results = reader.readtext(image)

    # Combine the results into a single string
    extracted_text = ' '.join([result[1] for result in results])

    return extracted_text

# Initialize results dictionary
results = {}

# Load models
license_plate_detector = YOLO('license_plate_detector.pt')

# Load image
image_path = "4.png"
frame = cv2.imread(image_path)

# Detect license plates
license_plates = license_plate_detector(frame)[0]

for license_plate in license_plates.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = license_plate

    # Crop license plate
    license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]

    # Preprocess the cropped license plate
    license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
    license_plate_crop_gray = cv2.resize(license_plate_crop_gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Display the cropped license plate
    plt.imshow(cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2RGB))
    plt.title('Cropped License Plate')
    plt.axis('off')  # Hide axes
    plt.show()

    # Extract text from the cropped license plate image
    text = extract_text_from_image(license_plate_crop_thresh)
    print(f"Detected text: {text}")

    # Save the result
    results[(x1, y1, x2, y2)] = text

# Optionally, save the results to a CSV file
# write_csv('results.csv', results)
