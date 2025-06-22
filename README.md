# ACBLAB Defect Deepfake Demo

## Overview
This project demonstrates two key functionalities via two Python scripts:

1. **Face-Swap Generation**: `defect_generator.py`  
2. **Deepfake Detection**: `defect_detector.py`  

Both scripts use hardcoded file paths—no command-line arguments are required.

## Setup
1. Open `defect_generator.py` and edit these variables at the top of the file:
   ```python
   source_path = "./data/source/source.jpg"
   target_path = "./data/target/target.jpg"
   output_path = "./results/swapped.jpg"
   ```
2. Open `defect_detector.py` and edit:
   ```python
   image_path = "./results/swapped.jpg"
   model_path = "./models/pretrained_detector.pth"
   ```
3. Ensure your folder structure matches:
   ```
   data/source/
   data/target/
   results/
   models/
   ```
4. Run each script with Python:
   ```bash
   python defect_generator.py
   python defect_detector.py
   ```

## Troubleshooting
- **Path Errors**:  
  - If the script cannot find an image or model file, double‑check the variables you edited for typos and correct folder names.
- **Memory Errors**:  
  - In `defect_generator.py`, before processing, you can resize the images:
    ```python
    import cv2
    img = cv2.imread(source_path)
    img = cv2.resize(img, (256, 256))
    ```
- **Model Loading Issues**:  
  - In `defect_detector.py`, ensure `torch.load(model_path, map_location="cpu")` if you don’t have a GPU.
- **Permissions**:  
  - If you get a permission denied error writing results, check that `results/` is writable:
    ```bash
    chmod +w results/
    ```

## License
MIT
