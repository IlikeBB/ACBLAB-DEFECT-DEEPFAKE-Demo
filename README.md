# ACBLAB Defect Deepfake Demo

## Overview
This repository contains two CPU-only Python scripts for:
1. **Face-Swap Generation** (`defect_generator.py`)  
2. **Deepfake Detection** (`defect_detector_hf.py`)

Each script uses hardcoded paths. Edit configuration variables at the top of each file before running.

## Prerequisites
- Python 3.8+
- Git (for cloning MobileFaceSwap)
- Internet connection (for downloading HuggingFace model)

## Installation
Install required Python packages:
```bash
pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm
```
> **Note:** For `paddlepaddle`, choose the correct package for your CPU platform, e.g. `pip install paddlepaddle`.

Clone the MobileFaceSwap repository next to `defect_generator.py`:
```bash
git clone https://github.com/IlikeBB/MobileFaceSwap.git
```

## Directory Structure
```
ACBLAB-DEFECT-DEEPFAKE-Demo/
├── defect_generator.py
├── defect_detector_hf.py
├── MobileFaceSwap/              # clone here
├── data/
│   ├── source/source.jpg        # input face for generator
│   └── target/                  # single image or folder for generator
├── results/                     # outputs will be saved here
├── models/
│   └── pretrained_detector.pth  # (optional) local HF model cache
```

## Configuration
### defect_generator.py
Edit the top section:
```python
SOURCE = r"<path to aligned source face image>"
TARGET = r"<path or directory of target image(s)>"
OUTPUT_DIR = "results"
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")
WEIGHT_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
```

### defect_detector_hf.py
Edit the top section:
```python
IMAGE_PATH = r"<path to image file to test>"
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

## Troubleshooting
1. **ModuleNotFoundError**  
   - Ensure all packages are installed (`torch`, `transformers`, `paddlepaddle`, etc.).  
   - For `paddlepaddle`, install the correct CPU-only version.

2. **MobileFaceSwap Repo Not Found**  
   - Confirm `MobileFaceSwap/` folder is in the same directory as `defect_generator.py`.  
   - Folder name must match `GITHUB_PROJECT_PATH` variable.

3. **FileNotFoundError (IMAGE_PATH or model path)**  
   - Verify path strings in each script—watch for backslashes (`\`) on Windows or raw strings.  
   - Ensure files exist and paths are correct.

4. **HuggingFace Model Download Issues**  
   - Check internet connection.  
   - If rate-limited, pre-download model to `~/.cache/huggingface/transformers` or specify `cache_dir`.

5. **Image Decode Failure**  
   - For non-ASCII paths, `imread_unicode` handles long or Unicode file names.  
   - If still failing, move images to a simple path (e.g., `C:/data/source.jpg`).

6. **Dimension Mismatch**  
   - In generator, input images must be resized to 224×224 before model inference.  
   - In detector, HF processor expects standard image formats (`RGB`).

7. **Memory Constraints**  
   - Both scripts run on CPU; large images may be slow.  
   - Resize images to 256×256 or smaller to speed up processing.

8. **PermissionError**  
   - Ensure `results/` folder is writable:  
     ```bash
     chmod +w results/
     ```

## License
MIT
