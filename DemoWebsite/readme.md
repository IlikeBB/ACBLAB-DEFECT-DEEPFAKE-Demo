# ACBLAB-DEFECT-DEEPFAKE-Demo

---

## Project Setup / 專案設定

+ Clone the [MobileFaceSwap](https://github.com/justinpinkney/MobileFaceSwap) repository:
   ```bash
   git clone https://github.com/justinpinkney/MobileFaceSwap.git
   cd MobileFaceSwap
   # Follow its README to install dependencies
   ```
---

## Project Structure / 專案結構

- **`./manage.py`**: Django management script (start server, migrations).  
  Django 管理腳本（啟動伺服器、資料庫遷移）
- **`./deepfake_site/settings.py`**: Django settings.  
  專案設定檔
- **`./deepfake_site/urls.py`**: URL routing configuration.  
  路由設定
- **`./forgery_detector/views.py`**: Handles upload, swap, and detect requests.  
  處理檔案上傳、換臉和檢測請求
- **`./forgery_detector/predict.py`**: Core detection function `detect_deepfake(...)`.  
  偵測函式實作
- **`./forgery_detector/templates/forgery_detector/dashboard.html`**: Main UI template with multilingual support.  
  前端介面模板，支援中英切換

---

## Django Construction / Django 架構說明

- **manage.py**: Launches the development server and runs commands.  
  啟動開發伺服器並執行 Django 命令
- **deepfake_site/urls.py**: Directs root path to the `forgery_detector` app.  
  將根路由導向 `forgery_detector` 應用
- **`./forgery_detector/views.py`**: Main view handling logic for face swap demo

  - Implements `dashboard(request)` which:
    1. On GET, clears session and media/resource folders
    2. On POST with `action='upload'`, saves source (A) and target (B) images with UUID filenames
    3. On POST with `action='swap'`, calls `face_swap(src_path, dst_path, swap_path)` and stores result
    4. Retrieves URLs for A, B, and swap results from session for template rendering

- **`./forgery_detector/predict.py`**: Core detection function `detect_deepfake(...)`.
- **`./forgery_detector/templates/forgery_detector/dashboard.html`**: Main UI template with multilingual support. Renders forms, previews, and Chart.js results, with language toggle script.  
  呈現表單、預覽及圖表，並支援語言切換腳本

---

## Quick Start / 快速上手

### Generate a deepfake / 生成深偽影像
```bash
# Start Django server
python manage.py runserver 0.0.0.0:8000

# In another terminal, run the generator
python defect_generator.py \
  --source path/to/source.jpg \
  --target path/to/target.jpg \
  --output results/
```
