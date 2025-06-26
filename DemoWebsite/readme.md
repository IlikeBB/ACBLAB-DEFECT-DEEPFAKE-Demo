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

## Quick Start / 快速上手

### Generate a deepfake / 生成深偽影像

```bash
cd deepfake_site
python manage.py runserver 0.0.0.0:8000
# or from repo root if manage.py is here
# python manage.py runserver 0.0.0.0:8000
```
