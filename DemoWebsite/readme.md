# ACBLAB-DEFECT-DEEPFAKE-Demo

---

## <span class="lang-en">Project Structure</span><span class="lang-zh">專案結構</span>

```bash
deepfake_site/            # Django project root
├── manage.py             # Django management script
├── deepfake_site/        # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── forgery_detector/     # Django app for swap & detection
│   ├── __init__.py
│   ├── forms.py          # Defines upload & detection forms
│   ├── predict.py        # Inference logic (detect_deepfake)
│   ├── urls.py           # App URL routes
│   ├── views.py          # Handles upload, swap, detect actions
│   └── templates/forgery_detector/
│       └── dashboard.html  # Main HTML template (multilang)
├── media/                # Uploaded source/target images
└── resources/            # Generated swap outputs
```

---

## <span class="lang-en">Install Dependencies</span><span class="lang-zh">安裝相依套件</span><span class="lang-zh">安裝相依套件</span></span><span class="lang-zh">安裝相依套件</span>

<span class="lang-en">
```bash
pip install \
  torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118 \
  transformers safetensors pillow numpy opencv-python \
  sklearn matplotlib flask \
  paddlepaddle==2.5.2.post101  # CPU-only Paddle
```
</span>
<span class="lang-zh">
```bash
pip install \
  torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118 \
  transformers safetensors pillow numpy opencv-python \
  sklearn matplotlib flask \
  paddlepaddle==2.5.2.post101  # 僅 CPU 版 Paddle
```
</span>

---

## <span class="lang-en">Quick Start</span><span class="lang-zh">快速上手</span>

<span class="lang-en">
1. **Generate a deepfake**  
   ```bash
   python defect_generator.py --source path/to/source.jpg --target path/to/target.jpg --output results/
   ```

2. **Detect deepfake**  
   ```bash
   python defect_detector.py --image path/to/image.jpg --model MODEL_NAME
   ```

> Outputs and generated images will be saved under `results/` by default.
</span>
<span class="lang-zh">
1. **生成深偽影像**  
   ```bash
   python defect_generator.py --source path/to/source.jpg --target path/to/target.jpg --output results/
   ```

2. **檢測深偽影像**  
   ```bash
   python defect_detector.py --image path/to/image.jpg --model MODEL_NAME
   ```

> 輸出與生成的影像預設存放於 `results/` 資料夾。
</span>

---

## <span class="lang-en">Common Pitfalls</span><span class="lang-zh">常見問題</span>

<span class="lang-en">
- **CUDA mismatch**: Ensure your GPU driver matches PyTorch CUDA version (`cu118`).
- **OpenSSL error** (`libssl.so.1.1`):  
  ```bash
  conda install openssl=1.1
  ```
- **Paddle import errors**:  
  ```bash
  pip uninstall paddlepaddle paddlepaddle-gpu
  pip install paddlepaddle==2.5.2.post101
  ```
</span>
<span class="lang-zh">
- **CUDA 版本不符**：確保你的顯卡驅動與 PyTorch CUDA (`cu118`) 相容。
- **OpenSSL 錯誤** (`libssl.so.1.1`)：  
  ```bash
  conda install openssl=1.1
  ```
- **Paddle 載入失敗**：  
  ```bash
  pip uninstall paddlepaddle paddlepaddle-gpu
  pip install paddlepaddle==2.5.2.post101
  ```
</span>
