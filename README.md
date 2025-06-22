# ACBLAB Defect Deepfake Demo

<details>
<summary>🇬🇧 English</summary>

---

## Demo WebSite
**Demo Web:** [Link](http://140.113.164.91:8888)  
<img src="https://github.com/user-attachments/assets/e32f0297-50b3-4b89-8813-5f83e0dc2cc5" alt="Demo Screenshot" width="100%" />

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
├── MobileFaceSwap/
├── data/
│   ├── source/source.jpg
│   └── target/
├── results/
└── models/
    └── pretrained_detector.pth
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
> **Note:** Download the pretrained weights from  
> https://github.com/Seanseattle/MobileFaceSwap/blob/main/checkpoints/MobileFaceSwap_224.pdparams?raw=true

### defect_detector_hf.py
At the top of the file, set:
```python
IMAGE_PATH = "<path to test image>"
HF_MODEL   = "prithivMLmods/open-deepfake-detection"
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
- MobileFaceSwap GitHub Repository: https://github.com/Seanseattle/MobileFaceSwap  
- HuggingFace Deepfake Models: https://huggingface.co/models?sort=downloads&search=deepfake

## Troubleshooting
1. **Missing Python Modules**  
2. **MobileFaceSwap Not Found**  
3. **FileNotFoundError**  
4. **HuggingFace Download Fails**  
5. **Image Read/Decode Errors**  
6. **Dimension/Resize Issues**  
7. **Out of Memory / Performance**  
8. **Permission Denied**

## License
MIT

---
</details>

<details>
<summary>🇹🇼 繁體中文</summary>

---

## 示範網站
**示範網址：** [點此進入](http://140.113.164.91:8888)  
<img src="https://github.com/user-attachments/assets/e32f0297-50b3-4b89-8813-5f83e0dc2cc5" alt="Demo Screenshot" width="100%" />

## 概述
本儲存庫包含兩個僅限 CPU 的 Python 腳本：
1. **人臉置換生成** (`defect_generator.py`)  
2. **深偽偵測** (`defect_detector_hf.py`)

兩者皆採硬編碼路徑，請在執行前於檔案頂部修改相關變數。

## 先決條件
- Python 3.8 或以上  
- Git  
- 網路連線

## 安裝
```bash
pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm
```
克隆 MobileFaceSwap：
```bash
git clone https://github.com/Seanseattle/MobileFaceSwap.git
```

## 目錄結構
```
ACBLAB-DEFECT-DEEPFAKE-Demo/
├── defect_generator.py
├── defect_detector_hf.py
├── MobileFaceSwap/
├── data/
│   ├── source/source.jpg
│   └── target/
├── results/
└── models/
    └── pretrained_detector.pth
```

## 配置
### defect_generator.py
```python
SOURCE = "<對齊後來源圖像路徑>"
TARGET = "<目標圖像路徑>"
OUTPUT_DIR = "results"
```
> 下載權重: https://github.com/Seanseattle/MobileFaceSwap/blob/main/checkpoints/MobileFaceSwap_224.pdparams?raw=true

### defect_detector_hf.py
```python
IMAGE_PATH = "<待測試圖像路徑>"
HF_MODEL   = "prithivMLmods/open-deepfake-detection"
```

## 使用
```bash
python defect_generator.py
python defect_detector_hf.py
```

## 相關連結
- https://github.com/Seanseattle/MobileFaceSwap
- https://huggingface.co/models?sort=downloads&search=deepfake

## 故障排除
- 模組缺少  
- 儲存庫不存在  
- 檔案未找到  
- 下載失敗  
- 解碼錯誤  
- 尺寸問題  
- 記憶體不足  
- 權限被拒

## 授權
MIT

---
</details>
