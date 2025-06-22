# ACVLAB Defect Deepfake Demo
> **English (Educator’s Note):**
> In this demo, you’re not limited to the sample scripts provided. Today, there are numerous public resources and implementations for generating and detecting deepfakes—many on GitHub or HuggingFace. If you’re unsure where to start or need help with Python setup, refer first to the translated example scripts we’ve shared here, then try running them. Once you succeed, explore other models—perhaps you’ll find more accurate detectors or higher-quality face-swap generators to test your data.
> 
> Demo slide deck: [slide link here](https://www.canva.com/design/DAGqtDjaouo/8iTYQu4UZHARx_ToNfnh4w/edit?utm_content=DAGqtDjaouo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

> **中文（教學者說明）：**
> 在本次示範中，不必侷限於使用範例腳本。現今生成與偵測深偽造的公開資源豐富，無論是 GitHub 上的程式碼或 HuggingFace 上的模型，都可下載並測試。如果不確定如何開始，或對 Python 環境設置仍有疑問，可先參考我們提供的翻譯範例程式並嘗試執行；成功後，再尋找更準確的偵測器或更優質的人臉置換生成器來驗證數據。
> 
> 示範簡報：在此查看 [簡報連結](https://www.canva.com/design/DAGqtDjaouo/8iTYQu4UZHARx_ToNfnh4w/edit?utm_content=DAGqtDjaouo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


<details>
<summary>🇬🇧 English</summary>

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
- Git (to clone [MobileFaceSwap](https://github.com/Seanseattle/MobileFaceSwap))  
- Internet connection (for downloading the [HuggingFace model](https://huggingface.co/models?sort=downloads&search=deepfake))

## Installation
Install required Python packages:
```bash
pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm
```

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
> [Google Drive](https://drive.google.com/file/d/1ZIzGLDB15GRAZAbkfNR0hNWdgQpxeA_r/view)

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
- Git（用於克隆 [MobileFaceSwap](https://github.com/Seanseattle/MobileFaceSwap))  
- 網路連線（用於下載 [HuggingFace 模型](https://huggingface.co/models?sort=downloads&search=deepfake))
## 安裝
安裝所需的 Python 套件：
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
> [Google Drive](https://drive.google.com/file/d/1ZIzGLDB15GRAZAbkfNR0hNWdgQpxeA_r/view)
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

