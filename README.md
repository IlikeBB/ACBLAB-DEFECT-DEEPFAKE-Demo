# ACBLAB Defect Deepfake Demo

> **Note:** During the demo, you are not limited to using this code base.  
> If you find better face-swap or deepfake detection implementations on GitHub or HuggingFace, feel free to integrate them instead of (or alongside) this demo package.

<details>
<summary>🇬🇧 English</summary>

---

## Demo WebSite
**Demo Web:** [Link](http://140.113.164.91:8888)  
<img src="https://github.com/user-attachments/assets/e32f0297-50b3-4b89-8813-5f83e0dc2cc5" alt="Demo Screenshot" width="100%" />

## Overview
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
- **MobileFaceSwap GitHub Repository**: https://github.com/Seanseattle/MobileFaceSwap  
- **HuggingFace Deepfake Models**: https://huggingface.co/models?sort=downloads&search=deepfake  
- **PyTorch Previous Versions**: https://pytorch.org/get-started/previous-versions/  
  *Use this link to download and install a specific PyTorch release compatible with your CUDA or CPU setup.*  
- **Miniconda Installer**: https://www.anaconda.com/docs/getting-started/miniconda/install  
  *Miniconda provides a lightweight environment manager for creating isolated Python environments.*  
- **HuggingFace Hub**: https://huggingface.co  
  *Explore and download open-source models, datasets, and more from the HuggingFace community.*

## Troubleshooting Examples
1. **Missing Python Modules**  
   - *Error:* `ModuleNotFoundError: No module named 'torch'`  
   - *Reason:* Required package not installed.  
   - *Solution:* `pip install torch torchvision`

2. **File Not Found**  
   - *Error:* `FileNotFoundError: [Errno 2] No such file or directory: 'data/source/source.jpg'`  
   - *Reason:* IMAGE_PATH or SOURCE path is incorrect or file missing.  
   - *Solution:* Check the path variable and ensure the file exists.

3. **HuggingFace Model Download Timeout**  
   - *Error:* `HTTPError: Connection timed out`  
   - *Reason:* Network issues or rate limits.  
   - *Solution:* Pre-download the model manually:  
     ```bash
     transformers-cli download prithivMLmods/open-deepfake-detection
     ```

4. **Image Decode Failure**  
   - *Error:* `cv2.error: unsupported or invalid image format`  
   - *Reason:* Incorrect image format or corrupted file.  
   - *Solution:* Convert to `.png` or `.jpg`, or use `imread_unicode` for long paths.

5. **Memory Exhaustion**  
   - *Error:* `RuntimeError: CUDA out of memory` or slow CPU processing  
   - *Reason:* Large image sizes.  
   - *Solution:* Resize images to 256×256 or smaller.

6. **Permission Denied**  
   - *Error:* `PermissionError: [Errno 13] Permission denied: 'results/'`  
   - *Reason:* Output directory not writable.  
   - *Solution:*  
     ```bash
     chmod +w results/
     ```

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
- Git（用於克隆 MobileFaceSwap）  
- 網路連線（用於下載 HuggingFace 模型）

## 安裝
安裝所需的 Python 套件：
```bash
pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm
```
> 若僅需 CPU 版本 PaddlePaddle，請參考 https://www.paddlepaddle.org.cn/install/quick。

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
在檔案頂部設定：
```python
SOURCE = "<對齊後來源圖像路徑>"
TARGET = "<目標圖像或資料夾路徑>"
OUTPUT_DIR = "results"
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")
WEIGHT_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
```
> **注意：** 請從  
> https://github.com/Seanseattle/MobileFaceSwap/blob/main/checkpoints/MobileFaceSwap_224.pdparams?raw=true  
> 下載預訓練權重檔。

### defect_detector_hf.py
在檔案頂部設定：
```python
IMAGE_PATH = "<待測試圖像路徑>"
HF_MODEL   = "prithivMLmods/open-deepfake-detection"
```

## 使用方式
執行人臉置換：
```bash
python defect_generator.py
```
執行深偽偵測：
```bash
python defect_detector_hf.py
```

## 相關連結
- **MobileFaceSwap GitHub 儲存庫**： https://github.com/Seanseattle/MobileFaceSwap  
- **HuggingFace 深偽模型**： https://huggingface.co/models?sort=downloads&search=deepfake  
- **PyTorch 舊版本下載**： https://pytorch.org/get-started/previous-versions/  
  *可從此下載與您的 CUDA/CPU 相容的特定 PyTorch 版本。*  
- **Miniconda 安裝指南**： https://www.anaconda.com/docs/getting-started/miniconda/install  
  *使用 Miniconda 建立隔離的 Python 虛擬環境。*  
- **HuggingFace Hub**： https://huggingface.co  
  *探索並下載開源模型、資料集等資源。*

## 故障排除示例
1. **缺少 Python 套件**  
   - *錯誤:* `ModuleNotFoundError: No module named 'torch'`  
   - *原因:* 未安裝必要套件  
   - *解決:*  
     ```bash
     pip install torch torchvision
     ```

2. **檔案未找到**  
   - *錯誤:* `FileNotFoundError: [Errno 2] No such file or directory: 'data/source/source.jpg'`  
   - *原因:* 路徑錯誤或檔案不存在  
   - *解決:* 確認檔案路徑及名稱

3. **HuggingFace 下載逾時**  
   - *錯誤:* `HTTPError: Connection timed out`  
   - *原因:* 網路或速率限制  
   - *解決:*  
     ```bash
     transformers-cli download prithivMLmods/open-deepfake-detection
     ```

4. **影像解碼失敗**  
   - *錯誤:* `cv2.error: unsupported or invalid image format`  
   - *原因:* 圖片格式不支援或損毀  
   - *解決:* 轉檔為 `.jpg` 或 `.png`，或使用 `imread_unicode`

5. **記憶體不足**  
   - *錯誤:* `RuntimeError: CUDA out of memory`  
   - *原因:* 圖片過大  
   - *解決:* 調整為 256×256 或更小

6. **權限被拒**  
   - *錯誤:* `PermissionError: [Errno 13] Permission denied: 'results/'`  
   - *原因:* 無寫入權限  
   - *解決:*  
     ```bash
     chmod +w results/
     ```

## 授權
MIT

---
</details>

