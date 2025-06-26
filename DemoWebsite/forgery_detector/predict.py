import subprocess
import os
import sys

MODEL_ROOT = "/ssd7/chih/DeepFake_WebDemo/MobileFaceSwap/"
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
        "--use_gpu", "True"
    ]
    print(f">> [predict] 執行指令: {' '.join(cmd)}")
    env = os.environ.copy()
    env["PYTHONPATH"] = MODEL_ROOT

    result = subprocess.run(cmd, capture_output=True, env=env, text=True)
    print(f">> [predict] returncode={result.returncode}")
    print(">> [predict] stdout:\n", result.stdout)
    print(">> [predict] stderr:\n", result.stderr)

    if result.returncode != 0:
        raise RuntimeError(f"[predict] 換臉腳本錯誤: {result.stderr}")

    if not os.path.exists(out_path):
        raise FileNotFoundError(f"[predict] 未找到預期輸出: {out_path}")

    print(f">> [predict] 換臉結果檔案已生成: {out_path}")
    return out_path
