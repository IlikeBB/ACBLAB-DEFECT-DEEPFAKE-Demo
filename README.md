# ACBLAB-DEFECT-DEEPFAKE-Demo

---

## Overview

Two example scripts for deepfake experiments:

1. **`defect_generator.py`**  
   Generate a face-swap result given a source and a target image.
2. **`defect_detector.py`**  
   Load a pretrained classifier to decide whether an image is real or fake.

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

Open a ready-to-run notebook (no local install needed):  
https://colab.research.google.com/github/YOUR_USER/YOUR_REPO/blob/main/Deepfake_Demo.ipynb

---

## Install Dependencies

\`\`\`bash
pip install \
  torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118 \
  transformers safetensors pillow numpy opencv-python \
  sklearn matplotlib flask \
  paddlepaddle==2.5.2.post101
\`\`\`

> _For CPU-only Paddle, install exactly the version above._

---

## Quick Start

1. **Generate a deepfake**  
   \`\`\`bash
   python defect_generator.py \
     --source path/to/source.jpg \
     --target path/to/target.jpg \
     --output results/
   \`\`\`

2. **Detect deepfake**  
   \`\`\`bash
   python defect_detector.py \
     --image  path/to/image.jpg \
     --model  MODEL_NAME
   \`\`\`

> Outputs and generated images will be saved under \`results/\` by default.

---

## Common Pitfalls

- **CUDA mismatch**: Ensure your GPU driver matches PyTorch CUDA version (\`cu118\`).  
- **OpenSSL error** (\`libssl.so.1.1\`):  
  \`\`\`bash
  conda install openssl=1.1
  \`\`\`  
- **Paddle import errors**:  
  \`\`\`bash
  pip uninstall paddlepaddle paddlepaddle-gpu
  pip install paddlepaddle==2.5.2.post101
  \`\`\`

---

> Copy this \`README.md\` into your repository root and add your two scripts.
