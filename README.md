# Krishan-kumar-wasserstoff-AiInternTask
## Overview
This project implements an AI pipeline that segments objects within an input image, extracts and identifies these objects, summarizes their attributes, and displays the results through an interactive Streamlit web interface. The pipeline leverages various deep learning models and image processing libraries to achieve these tasks.

## Features
**Image Segmentation:** Uses Mask R-CNN to segment objects in images. <br>
**Object Identification:** Identifies objects using Faster R-CNN.<br>
**Text Extraction:** Extracts text from segmented objects using Tesseract OCR.<br>
**Text Summarization:** Summarizes extracted text using NLP models.<br>
**Interactive UI:** Provides an interactive Streamlit web interface for image upload and processing.<br>
**Data Mapping:** Maps object data and attributes to the original image.<br>


## Project Structure
.
├── app.py                  # Streamlit app script<br>
├── README.md               # Project README file<br>
├── requirements.txt        # List of required Python packages<br>
├── data/                   # Directory for storing input and output data<br>
│   ├── input_images/       # Directory for input images<br>
│   ├── segmented_objects/  # Directory for segmented object images<br>
│   └── output/             # Directory for output data (JSON, CSV)<br>
└── scripts/                # Directory for additional scripts (if any)<br>

## Workflow
### 1. Image Segmentation:
* Uses Mask R-CNN to segment objects within an image.
* Saves segmented objects as separate images.
### 2. Object Identification:
* Identifies each object using Faster R-CNN.
* Extracts text from each object using Tesseract OCR.
### 3.Text Summarization:
* Summarizes the extracted text using NLP models.
### 4. Data Mapping:
* Maps object data, descriptions, extracted text, and summaries to the original image.
* Saves the mapping as a JSON file and generates a summary table.
### 5. Visualization and UI:
* Displays segmented images and summary tables through a Streamlit web interface.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

1. Fork the repository.
2. Create your feature branch (git checkout -b feature/your-feature-name).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature-name).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.








