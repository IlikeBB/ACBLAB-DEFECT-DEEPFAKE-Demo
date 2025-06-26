# ACBLAB-DEFECT-DEEPFAKE-Demo

---

## Project Structure / 專案結構

- **`./manage.py`**: Django launch and management script  
  Django 啟動與管理腳本
- **`./deepfake_site/settings.py`**: Site settings  
  網站設定
- **`./deepfake_site/urls.py`**: Global URL router  
  全域路由設定
- **`./forgery_detector/views.py`**: Handles upload, swap, detect actions  
  處理上傳、換臉、檢測三大動作
- **`./forgery_detector/predict.py`**: Implements `detect_deepfake(...)`  
  `detect_deepfake(...)` 函式實作
- **`./forgery_detector/templates/forgery_detector/dashboard.html`**: Main UI template with multilingual support  
  主畫面範本，支援多語切換
---

## Django Construction / Django 架構說明

- **manage.py**: Launches dev server and runs Django commands  
  啟動開發伺服器並執行 Django 命令
- **deepfake_site/urls.py**: Routes root URL to the `forgery_detector` app  
  將根路由導向 `forgery_detector` 應用
- **forgery_detector/views.py**: Defines views for three actions  
  定義三種主要的 view 操作
  1. `upload`: Save source/target or detection images  
     儲存來源/目標或檢測影像
  2. `swap`: Call `defect_generator.py` for face swap  
     呼叫 `defect_generator.py` 執行換臉
  3. `detect`: Use `detect_deepfake` from `predict.py`  
     使用 `predict.py` 中的 `detect_deepfake`
- **dashboard.html**: Renders the UI with Django template tags and language spans  
  使用 Django 模板與多語標籤渲染前端介面

---
