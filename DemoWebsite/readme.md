# ACBLAB-DEFECT-DEEPFAKE-Demo
---

## <span class="lang-en">Project Structure</span><span class="lang-zh">專案結構</span>

- **`./manage.py`**：Django 啟動與管理腳本。
- **`./deepfake_site/settings.py`**：網站設定。
- **`./deepfake_site/urls.py`**：全域路由。
- **`./forgery_detector/views.py`**：處理上傳、換臉、檢測三大動作。
- **`./forgery_detector/predict.py`**：`detect_deepfake(...)` 函式實作。
- **`./forgery_detector/templates/forgery_detector/dashboard.html`**：主頁面，多語切換與 UI。
- **`defect_generator.py`**：（放在根目錄）執行換臉流程。
- **`defect_detector.py`**：（放在根目錄）執行偽造檢測流程。

---

## <span class="lang-en">Django Construction</span><span class="lang-zh">Django 架構說明</span>

<span class="lang-en">
- **manage.py** launches the development server and handles commands.
- **deepfake_site/urls.py** routes root URL to `forgery_detector` app.
- **forgery_detector/views.py** defines three actions:
  - `upload` saves source/target or detection images.
  - `swap` calls `defect_generator.py` to perform face swap.
  - `detect` uses `detect_deepfake` from `predict.py` to classify images.
- **dashboard.html** in templates renders the UI, with Django template tags and language spans for dynamic content.
</span>
<span class="lang-zh">
- **manage.py** 啟動開發伺服器並處理 Django 命令。
- **deepfake_site/urls.py** 定義根路由，將請求導向 `forgery_detector` 應用。
- **forgery_detector/views.py** 實作三種操作：
  - `upload`：儲存來源/目標或檢測影像。
  - `swap`：呼叫 `defect_generator.py` 執行換臉。
  - `detect`：使用 `predict.py` 中的 `detect_deepfake` 進行偵測。
- **dashboard.html**（範本）負責渲染前端介面，結合 Django 模板語法與中英文切換標籤展示動態內容。
</span>
