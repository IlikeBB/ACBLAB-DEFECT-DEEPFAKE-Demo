# ACBLAB Defect Deepfake Demo

## Overview
This project demonstrates two key functionalities:

1. **Face-Swap Generation** using `defect_generator.py`  
   Swap a face from a source image onto a target image.

2. **Deepfake Detection** using `defect_detector.py`  
   Detect whether an image is real or fake with a pretrained model.

## Requirements
- Python 3.8 or above
- Packages (install via `pip install`):
  - torch
  - torchvision
  - opencv-python
  - numpy
  - pillow
  - argparse
  - tqdm

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/IlikeBB/ACBLAB-DEFECT-DEEPFAKE-Demo.git
   cd ACBLAB-DEFECT-DEEPFAKE-Demo
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install torch torchvision opencv-python numpy pillow argparse tqdm
   ```

## Data Preparation
- Place a source face image as `./data/source/source.jpg`
- Place a target face image as `./data/target/target.jpg`

Ensure images are approximately 256×256 pixels for optimal performance.

## Usage

### 1. Generate Face-Swap Result
```bash
python defect_generator.py   --source ./data/source/source.jpg   --target ./data/target/target.jpg   --output ./results/swapped.jpg
```
- `--source`: Path to source image  
- `--target`: Path to target image  
- `--output`: Path for the output image

If you encounter CUDA memory errors, try downsampling your images or run in CPU mode:
```bash
python defect_generator.py --device cpu ...
```

### 2. Detect Real vs. Fake
```bash
python defect_detector.py   --image ./results/swapped.jpg   --model ./models/pretrained_detector.pth
```
- `--image`: Path to the image to test  
- `--model`: Path to the pretrained detection model  

Example output:
```
P(Real)= 0.12
P(Fake)= 0.88
Label: Fake
```

## Troubleshooting
- **Module Not Found**: Ensure all packages are installed and your PYTHONPATH is correct.
- **File Not Found**: Verify that the paths for `--source`, `--target`, and `--model` are correct.
- **Memory Errors**: Reduce image size or switch to CPU mode.

## License
MIT

## Author
ACBLAB Training Team
