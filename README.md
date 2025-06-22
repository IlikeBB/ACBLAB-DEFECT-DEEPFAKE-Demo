# ACBLAB-DEFECT-DEEPFAKE-Demo

## Overview
This repository contains two example scripts:
- `defect_generator.py`: Generate a face-swap result from a source and a target image.
- `defect_detector.py`: Detect whether an image is real or fake using a pretrained model.

---

## Environment Setup

### Method A: Conda (recommended)
1. Install Miniconda: https://docs.conda.io/en/latest/miniconda.html  
2. Create & activate environment:
   ```bash
   conda create -n deepfake-demo python=3.9
   conda activate deepfake-demo
   ```

### Method B: Google Colab
Open and run without local setup:  
https://colab.research.google.com/github/YOUR_USER/YOUR_REPO/blob/main/Deepfake_Demo.ipynb

---

## Dependencies
Install required packages:
```bash
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118
pip install transformers pillow numpy opencv-python flask
pip install paddlepaddle==2.5.2.post101  # CPU-only Paddle
```

---

## Quick Start

1. **Generate a deepfake**  
   ```bash
   python defect_generator.py --source path/to/source.jpg --target path/to/target.jpg --output results/
   ```

2. **Detect deepfake**  
   ```bash
   python defect_detector.py --image path/to/image.jpg --model MODEL_NAME
   ```

---

> Replace `YOUR_USER` and `YOUR_REPO` with your GitHub username and repository name.
