# Improved Vision during Harsh Weather Conditions

## Project Overview

This project addresses the challenges faced by conventional object detection systems in adverse weather conditions, including fog, rain, and varying temperatures. Leveraging advanced YOLOv8 models fine-tuned with the Ultralytics library, the system processes input images from infrared, visible, and thermal spectrums. An innovative approach, enhancing visible images with infrared information, lays the groundwork for accurate predictions. The system refines predictions through a meticulous weighted fusion methodology, utilizing intersection over union (IoU) and model confidences. Deployment within a Jupyter Notebook environment showcases practicality and accessibility, emphasizing safety, ethics, and legal compliance.

## Key Features

- **Advanced YOLOv8 Models:** Utilizes state-of-the-art YOLOv8 models for robust object detection.
- **Multi-Spectrum Image Processing:** Processes infrared, visible, and thermal spectrum images for improved accuracy.
- **Weighted Fusion Methodology:** Enhances predictions through careful fusion of intersection over union (IoU) and model confidences.
- **Jupyter Notebook Deployment:** Demonstrates practicality and accessibility of the object detection system.

## Technical Details

### Programming Language
- **Python:** Primary language for algorithm implementation and workflow development.

### Image Processing Libraries
- **OpenCV:** Plays a crucial role in image loading, processing, and manipulation. Handles tasks such as color space conversion and image blending.

### Deep Learning Frameworks
- **PyTorch:** Foundation for training and working with deep learning models. Ultralytics YOLOv8, built on PyTorch, is employed for fine-tuning and object detection.

### Machine Learning Libraries
- **NumPy:** Utilized for numerical operations and array manipulation, particularly in tasks related to handling weights and bounding box calculations.

### Data Annotation and Conversion
- **Roboflow:** Source for the dataset containing thermal images. Functions as a tool for data annotation and conversion, essential in computer vision projects.

### Development Environment
- **Torch and Ultralytics Library:** Utilized for fine-tuning YOLOv8 models.
- **Jupyter Notebooks:** Serves as a versatile environment for project development.

## Contribution to the Field

This project addresses critical research gaps, providing a valuable solution for accurate object detection in challenging weather scenarios. The focus on safety standards, ethical considerations, and legal compliance ensures responsible use of the technology, contributing to enhanced road safety and surveillance efficacy.
