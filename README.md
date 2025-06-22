<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-i18n="title">ACBLAB Defect Deepfake Demo</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    header { margin-bottom: 20px; }
    button#lang-toggle { padding: 6px 12px; cursor: pointer; }
    section { margin-bottom: 24px; }
    h2 { margin-top: 16px; }
    pre { background: #f5f5f5; padding: 10px; overflow-x: auto; }
  </style>
</head>
<body>
  <header>
    <button id="lang-toggle">中文</button>
  </header>

  <section>
    <h2 data-i18n="demo_site">Demo WebSite</h2>
    <p>
      <strong>
        <a data-i18n="demo_link_text" href="http://140.113.164.91:8888">Demo Web</a>
      </strong>
    </p>
    <img
      src="https://github.com/user-attachments/assets/e32f0297-50b3-4b89-8813-5f83e0dc2cc5"
      alt="Demo Screenshot"
      style="max-width:100%; height:auto;"
    />
  </section>

  <section>
    <h2 data-i18n="overview_title">Overview</h2>
    <p data-i18n="overview_text">
      This repository contains two CPU-only Python scripts for Face-Swap Generation and Deepfake Detection.
    </p>
  </section>

  <section>
    <h2 data-i18n="prereq_title">Prerequisites</h2>
    <ul>
      <li data-i18n="prereq_python">Python 3.8 or above</li>
      <li data-i18n="prereq_git">Git (to clone MobileFaceSwap)</li>
      <li data-i18n="prereq_internet">
        Internet connection (for downloading the HuggingFace model)
      </li>
    </ul>
  </section>

  <section>
    <h2 data-i18n="install_title">Installation</h2>
    <p data-i18n="install_text">Install required Python packages:</p>
    <pre><code>pip install torch torchvision transformers pillow opencv-python numpy paddlepaddle tqdm</code></pre>
    <p data-i18n="install_note">
      For CPU-only PaddlePaddle, use the appropriate command from
      <a href="https://www.paddlepaddle.org.cn/install/quick">https://www.paddlepaddle.org.cn/install/quick</a>.
    </p>
    <p data-i18n="install_clone">
      Clone the MobileFaceSwap repository alongside <code>defect_generator.py</code>:
    </p>
    <pre><code>git clone https://github.com/Seanseattle/MobileFaceSwap.git</code></pre>
  </section>

  <section>
    <h2 data-i18n="dir_title">Directory Structure</h2>
    <pre><code>
ACBLAB-DEFECT-DEEPFAKE-Demo/
├── defect_generator.py
├── defect_detector_hf.py
├── MobileFaceSwap/              # clone here
├── data/
│   ├── source/source.jpg        # input for generator
│   └── target/                  # single image or folder for generator
├── results/                     # outputs; script creates if missing
└── models/
    └── pretrained_detector.pth  # optional local HF model cache
    </code></pre>
  </section>

  <section>
    <h2 data-i18n="config_title">Configuration</h2>

    <h3 data-i18n="config_gen_title">defect_generator.py</h3>
    <p data-i18n="config_gen_text">At the top of the file, set:</p>
    <pre><code>SOURCE = "&lt;path to aligned source image&gt;"
TARGET = "&lt;path or directory of target images&gt;"
OUTPUT_DIR = "results"
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")
WEIGHT_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
    </code></pre>
    <p data-i18n="config_gen_note">
      Note: Download the pretrained weights from
      <a href="https://github.com/Seanseattle/MobileFaceSwap/blob/main/checkpoints/MobileFaceSwap_224.pdparams?raw=true">
        here
      </a>.
    </p>

    <h3 data-i18n="config_det_title">defect_detector_hf.py</h3>
    <p data-i18n="config_det_text">At the top of the file, set:</p>
    <pre><code>IMAGE_PATH = "&lt;path to test image&gt;"
HF_MODEL   = "prithivMLmods/open-deepfake-detection"
    </code></pre>
  </section>

  <section>
    <h2 data-i18n="usage_title">Usage</h2>
    <p data-i18n="usage_gen">Run face-swap generation:</p>
    <pre><code>python defect_generator.py</code></pre>
    <p data-i18n="usage_det">Run deepfake detection:</p>
    <pre><code>python defect_detector_hf.py</code></pre>
  </section>

  <section>
    <h2 data-i18n="links_title">Related Links</h2>
    <ul>
      <li>
        <a
          href="https://github.com/Seanseattle/MobileFaceSwap"
          data-i18n="link_mfs"
          >MobileFaceSwap GitHub Repository</a
        >
      </li>
      <li>
        <a
          href="https://huggingface.co/models?sort=downloads&search=deepfake"
          data-i18n="link_hf"
          >HuggingFace Deepfake Models</a
        >
      </li>
    </ul>
  </section>

  <section>
    <h2 data-i18n="ts_title">Troubleshooting</h2>
    <ol>
      <li data-i18n="ts_mod">
        Missing Python Modules: Verify installation of <code>torch</code>,
        <code>transformers</code>, <code>paddlepaddle</code>, etc.
      </li>
      <li data-i18n="ts_repo">
        MobileFaceSwap Not Found: Ensure <code>MobileFaceSwap/</code> is in the
        same directory as <code>defect_generator.py</code>.
      </li>
      <li data-i18n="ts_file">
        FileNotFoundError: Double-check the path variables in each script for
        typos and correct separators.
      </li>
      <li data-i18n="ts_hf">
        HuggingFace Download Fails: Check your internet or use a cached model
        directory (<code>cache_dir</code> in HF).
      </li>
      <li data-i18n="ts_img">
        Image Read/Decode Errors: For Unicode or long paths, <code>imread_unicode</code>
        handles it; otherwise use simple paths.
      </li>
      <li data-i18n="ts_dim">
        Dimension/Resize Issues: Generator resizes inputs to 224×224; Detector
        expects RGB PIL images.
      </li>
      <li data-i18n="ts_mem">
        Out of Memory/Performance: Use smaller images (e.g., 256×256) to speed
        up.
      </li>
      <li data-i18n="ts_perm">
        Permission Denied: Ensure <code>results/</code> is writable
        (<code>chmod +w results/</code>).
      </li>
    </ol>
  </section>

  <footer>
    <p data-i18n="license">MIT License</p>
  </footer>

  <script>
    const translations = {
      en: {
        title: "ACBLAB Defect Deepfake Demo",
        demo_site: "Demo WebSite",
        demo_link_text: "Demo Web",
        overview_title: "Overview",
        overview_text:
          "This repository contains two CPU-only Python scripts for Face-Swap Generation and Deepfake Detection.",
        prereq_title: "Prerequisites",
        prereq_python: "Python 3.8 or above",
        prereq_git: "Git (to clone MobileFaceSwap)",
        prereq_internet:
          "Internet connection (for downloading the HuggingFace model)",
        install_title: "Installation",
        install_text: "Install required Python packages:",
        install_note:
          "For CPU-only PaddlePaddle, use the appropriate command from https://www.paddlepaddle.org.cn/install/quick.",
        install_clone:
          "Clone the MobileFaceSwap repository alongside defect_generator.py:",
        dir_title: "Directory Structure",
        config_title: "Configuration",
        config_gen_title: "defect_generator.py",
        config_gen_text: "At the top of the file, set:",
        config_gen_note: "Note: Download the pretrained weights from here.",
        config_det_title: "defect_detector_hf.py",
        config_det_text: "At the top of the file, set:",
        usage_title: "Usage",
        usage_gen: "Run face-swap generation:",
        usage_det: "Run deepfake detection:",
        links_title: "Related Links",
        link_mfs: "MobileFaceSwap GitHub Repository",
        link_hf: "HuggingFace Deepfake Models",
        ts_title: "Troubleshooting",
        ts_mod:
          "Missing Python Modules: Verify installation of torch, transformers, paddlepaddle, etc.",
        ts_repo:
          "MobileFaceSwap Not Found: Ensure MobileFaceSwap/ is in the same directory as defect_generator.py.",
        ts_file:
          "FileNotFoundError: Double-check the path variables in each script for typos and correct separators.",
        ts_hf:
          "HuggingFace Download Fails: Check your internet or use a cached model directory (cache_dir in HF).",
        ts_img:
          "Image Read/Decode Errors: For Unicode or long paths, imread_unicode handles it; otherwise use simple paths.",
        ts_dim:
          "Dimension/Resize Issues: Generator resizes inputs to 224×224; Detector expects RGB PIL images.",
        ts_mem:
          "Out of Memory/Performance: Use smaller images (e.g., 256×256) to speed up.",
        ts_perm:
          "Permission Denied: Ensure results/ is writable (chmod +w results/).",
        license: "MIT License"
      },
      zh: {
        title: "ACBLAB 缺陷深偽造示範",
        demo_site: "示範網站",
        demo_link_text: "示範網站連結",
        overview_title: "概述",
        overview_text:
          "本儲存庫包含兩個僅限 CPU 的 Python 腳本，用於人臉置換與深偽偵測。",
        prereq_title: "先決條件",
        prereq_python: "Python 3.8 或以上",
        prereq_git: "Git（用於克隆 MobileFaceSwap）",
        prereq_internet:
          "網路連線（用於下載 HuggingFace 模型）",
        install_title: "安裝",
        install_text: "安裝所需的 Python 套件：",
        install_note:
          "對於僅限 CPU 的 PaddlePaddle，請參考 https://www.paddlepaddle.org.cn/install/quick。",
        install_clone:
          "在 defect_generator.py 同級目錄下克隆 MobileFaceSwap 儲存庫：",
        dir_title: "目錄結構",
        config_title: "配置",
        config_gen_title: "defect_generator.py",
        config_gen_text: "在檔案頂部設定：",
        config_gen_note: "注意：請從此處下載預訓練權重。",
        config_det_title: "defect_detector_hf.py",
        config_det_text: "在檔案頂部設定：",
        usage_title: "使用方式",
        usage_gen: "執行人臉置換：",
        usage_det: "執行深偽偵測：",
        links_title: "相關連結",
        link_mfs: "MobileFaceSwap GitHub 儲存庫",
        link_hf: "HuggingFace 深偽模型",
        ts_title: "故障排除",
        ts_mod:
          "缺少 Python 模組：請確認已安裝 torch、transformers、paddlepaddle 等。",
        ts_repo:
          "找不到 MobileFaceSwap：請確保 MobileFaceSwap/ 與 defect_generator.py 位於同一目錄。",
        ts_file:
          "檔案未找到：檢查腳本中的路徑變數是否有錯字及正確的分隔符。",
        ts_hf:
          "HuggingFace 下載失敗：請檢查網路或使用快取模型目錄（HF 的 cache_dir）。",
        ts_img:
          "圖像讀取/解碼錯誤：對於 Unicode 或長路徑，可使用 imread_unicode；否則請使用簡單路徑。",
        ts_dim:
          "尺寸/調整問題：生成器會將輸入調整為 224×224；偵測器期望 RGB PIL 圖片。",
        ts_mem:
          "內存不足/效能問題：使用較小圖片（例如 256×256）以提升速度。",
        ts_perm:
          "權限被拒：請確保 results/ 可寫（chmod +w results/）。",
        license: "MIT 許可證"
      }
    };

    let currentLang = "en";
    const toggleBtn = document.getElementById("lang-toggle");

    toggleBtn.addEventListener("click", () => {
      currentLang = currentLang === "en" ? "zh" : "en";
      document.documentElement.lang = currentLang;
      toggleBtn.innerText = currentLang === "en" ? "中文" : "English";

      document.querySelectorAll("[data-i18n]").forEach((el) => {
        const key = el.getAttribute("data-i18n");
        if (translations[currentLang][key]) {
          el.textContent = translations[currentLang][key];
        }
      });
    });
  </script>
</body>
</html>
