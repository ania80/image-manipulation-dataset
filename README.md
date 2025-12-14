**Image Manipulation Dataset Generator**

**Overview**
A Python project that automatically generates multiple transformed versions of input images to create reproducible datasets for machine learning, especially in computer vision.

**Motivation**
Real-world images are often blurred, noisy, cropped, or compressed. ML models need to learn from such variations to perform well. This project focuses on **programmatically controlling image transformations** before feeding them into models.

**Features**
- Load multiple images from `images/` folder
- Apply transformations:
  - Original
  - Gaussian Blur
  - Gaussian Noise
  - Crop & Resize (center crop)
  - JPEG Compression
- Save transformed images in labeled folders under `output/`
- Scalable for any number of images
- 
**Project Structure**
image_dataset_project/
├─ images/ # Source images
├─ main.py # Dataset generator script
├─ output/ # Generated image variants
│ ├─ original/
│ ├─ blur/
│ ├─ noise/
│ ├─ crop_resize/
│ └─ jpeg/
└─ .venv/ # Virtual environment

**Tools Used**
- Python 3.13.5 
- OpenCV (image processing)  
- NumPy (numerical operations)  
- Git & GitHub (version control and project hosting)

**How to Use**
1. Place the images in the `images/` folder.
2. Activate the virtual environment:
   .venv\Scripts\activate
3. Install required packages (first time only):
   pip install numpy pillow opencv-python
4. Run the script:
   python main.py
5. Check the output/ folder for all transformed images.

**Next Steps**
- Expand transformations (rotation, brightness/contrast, color shift)
- Convert images to NumPy arrays for ML frameworks like PyTorch
- Create training and testing datasets automatically
- Begin experimenting with convolutional neural networks (CNNs) using the generated dataset

**Author: Aniya**
