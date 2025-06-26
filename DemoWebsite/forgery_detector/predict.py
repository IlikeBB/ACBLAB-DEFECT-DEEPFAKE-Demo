import subprocess
import os
import sys

# ─────────── 1. 動態找出專案根目錄 ───────────
# __file__ 在 forgery_detector/predict.py
HERE = os.path.dirname(__file__)            # .../deepfake_site/forgery_detector
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, os.pardir))  
# PROJECT_ROOT -> .../deepfake_site

PARENT = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
# PARENT -> 專案最上層資料夾 (Deep-Fake-WebDemo)

# ─────────── 2. 定義 MODEL_ROOT 與 SCRIPT 路徑 ───────────
MODEL_ROOT     = os.path.join(PARENT, "MobileFaceSwap")
IMG_TEST_SCRIPT = os.path.join(MODEL_ROOT, "image_test.py")

def face_swap(src_path, dst_path, out_path):
    python_exe = sys.executable
    cmd = [
        python_exe, IMG_TEST_SCRIPT,
        "--source_img_path", src_path,
        "--target_img_path", dst_path,
        "--output_dir", os.path.dirname(out_path),
        "--image_size", "224",
        "--merge_result", "True",
        "--need_align", "True",
        # "--use_gpu", "False"
        "--use_gpu", "True"
    ]
    print(f">> [predict] 執行指令: {' '.join(cmd)}")

    env = os.environ.copy()
    # 把 MODEL_ROOT 放到 PYTHONPATH，確保 image_test.py 能 import 到 utils
    env["PYTHONPATH"] = MODEL_ROOT

    # 呼叫子程序，拿 bytes，再自行 decode（跳過亂碼）
    result = subprocess.run(
        cmd,
        capture_output=True,
        env=env
    )
    out = result.stdout.decode("utf-8", errors="ignore")
    err = result.stderr.decode("utf-8", errors="ignore")

    print(f">> [predict] returncode={result.returncode}")
    print(">> [predict] stdout:\n", out)
    print(">> [predict] stderr:\n", err)

    if result.returncode != 0:
        raise RuntimeError(f"[predict] 換臉腳本錯誤: {err}")

    if not os.path.exists(out_path):
        raise FileNotFoundError(f"[predict] 未找到預期輸出: {out_path}")

    print(f">> [predict] 換臉結果檔案已生成: {out_path}")
    return out_path
