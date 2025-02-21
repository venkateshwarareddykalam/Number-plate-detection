# Number-plate-detection

This project detects and extracts vehicle number plates from images or video streams using computer vision techniques. It leverages OpenCV for image processing and Tesseract OCR for text recognition, making it suitable for applications like traffic monitoring or parking systems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:

git clone https://github.com/venkateshwarareddykalam/Number-plate-detection.git

2. Navigate to the project directory:

cd Number-plate-detection

3. Install the required dependencies:

pip install -r requirements.txt

Required libraries include:
- Python 3.8+
- OpenCV (`opencv-python`)
- Tesseract OCR (`pytesseract`)
- NumPy (`numpy`)
Install Tesseract OCR separately:
- On Ubuntu: `sudo apt install tesseract-ocr`
- On Windows/Mac: Download from [Tesseract’s GitHub](https://github.com/tesseract-ocr/tesseract) and add it to your PATH.

## Usage

Run the number plate detection script on an image or video file:

- For an image:

python detect_plates.py --input images/car.jpg --output output/detected_plate.jpg

- For a video:

python detect_plates.py --input videos/traffic.mp4 --output output/detected_video.mp4


Arguments:
- `--input`: Path to the input image or video file.
- `--output`: Path to save the output (optional).

The script processes the input, detects the number plate, extracts the text, and saves the result.

## Project Structure

Here’s an overview of the repository:

- `detect_plates.py`: Main script for detecting and extracting number plates.
- `requirements.txt`: List of Python dependencies.
- `images/`: Sample images for testing (e.g., `car.jpg`).
- `videos/`: Sample videos for testing (e.g., `traffic.mp4`).
- `output/`: Directory where detected results are saved.
- `utils.py`: Helper functions for image preprocessing and text extraction.

## Examples

1. Detect a number plate in an image:

python detect_plates.py --input images/car.jpg --output output/detected_plate.jpg

Expected output: An image with the number plate boxed and the extracted text printed (e.g., "ABC 1234").
Expected output: An image with the number plate boxed and the extracted text printed (e.g., "ABC 1234").
![Input Image](1.jpg)
![Detected Plate](reults.png)

2. Process a video:

2. Process a video:

python detect_plates.py --input videos/traffic.mp4 --output output/detected_video.mp4

Expected output: A video with number plates highlighted in each frame.

Sample result:
- Input: A car image with plate "XYZ 5678".
- Output: Image with a rectangle around the plate and text "XYZ 5678" logged to the console.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a branch for your feature or fix (`git checkout -b feature/new-idea`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature/new-idea`).
5. Open a pull request with a clear description of your changes.

For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact [venkateshwarareddykalam](https://github.com/venkateshwarareddykalam) via GitHub or open an issue on this repository.

---