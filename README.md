# ACBLAB Defect Deepfake Demo

## Overview
This repository contains two CPU-only Python scripts for:
1. **Face-Swap Generation** (`defect_generator.py`)  
2. **Deepfake Detection** (`defect_detector_hf.py`)

Both scripts use hardcoded paths. Edit configuration variables at the top of each file before running.

## Prerequisites
- Python 3.8 or above
- Git (to clone MobileFaceSwap)
- Internet connection (for downloading the HuggingFace model)

## Installation
Install required Python packages:
```bash
pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm
```
> For CPU-only PaddlePaddle, use the appropriate command from https://www.paddlepaddle.org.cn/install/quick.

Clone the MobileFaceSwap repository alongside `defect_generator.py`:
```bash
git clone https://github.com/Seanseattle/MobileFaceSwap.git
```

## Directory Structure
```
ACBLAB-DEFECT-DEEPFAKE-Demo/
├── defect_generator.py
├── defect_detector_hf.py
├── MobileFaceSwap/              # clone here
├── data/
│   ├── source/source.jpg        # input for generator
│   └── target/                  # single image or folder for generator
├── results/                     # outputs; script creates if missing
└── models/
    └── pretrained_detector.pth  # optional local HF model cache
```

## Configuration
### defect_generator.py
At the top of the file, set:
```python
SOURCE = "<path to aligned source image>"
TARGET = "<path or directory of target images>"
OUTPUT_DIR = "results"
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")
WEIGHT_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
```

### defect_detector_hf.py
At the top of the file, set:
```python
IMAGE_PATH = "<path to test image>"
HF_MODEL = "prithivMLmods/open-deepfake-detection"
```

## Usage
Run face-swap generation:
```bash
python defect_generator.py
```

Run deepfake detection:
```bash
python defect_detector_hf.py
```

## Related Links
- **MobileFaceSwap GitHub Repository:** https://github.com/Seanseattle/MobileFaceSwap  
- **HuggingFace Deepfake Models:** https://huggingface.co/models?sort=downloads&search=deepfake  

## Troubleshooting
1. **Missing Python Modules**  
   - Verify installation of `torch`, `transformers`, `paddlepaddle`, etc.

2. **MobileFaceSwap Not Found**  
   - Ensure `MobileFaceSwap/` is in the same directory as `defect_generator.py`.

3. **FileNotFoundError**  
   - Double-check the path variables in each script for typos and correct separators.

4. **HuggingFace Download Fails**  
   - Check your internet or use a cached model directory (`cache_dir` in HF).

5. **Image Read/Decode Errors**  
   - For Unicode or long paths, `imread_unicode` handles it; otherwise use simple paths.

6. **Dimension or Resize Issues**  
   - Generator: input images resized to 224×224 within the script.  
   - Detector: processor expects RGB PIL images.

7. **Out of Memory / Performance**  
   - Both scripts run on CPU; use smaller images (e.g., 256×256) to speed up.

8. **Permission Denied**  
   - Ensure `results/` is writable:
     ```bash
     chmod +w results/
     ```

## License
MIT
