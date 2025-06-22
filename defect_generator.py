# defect_generator.py
"""
MobileFaceSwap-based Face Swap Script (CPU Only)
使用 MobileFaceSwap 模型生成偽造人臉 / Generate deepfake faces using MobileFaceSwap

1. 將 MobileFaceSwap GitHub Repo 放在與此腳本同一層的資料夾 (名稱同為 "MobileFaceSwap")
2. 執行：python defect_generator.py
"""
import os
import sys
import cv2
import paddle

# === CONFIGURATION ===
# 本腳本路徑 / Script directory
dir_here = os.path.dirname(os.path.abspath(__file__))
# GitHub Repo 路徑，預期學生將 repo clone 到與此腳本同層的資料夾
# If repo folder named "MobileFaceSwap" in same directory as this script
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")

SOURCE = r"C:\Users\ru035\Desktop\Icloud\iCloudDrive\Documents\DeepFake_WebDemo\deepfake_site\media\a_53f98b047b194b5f9c7198e98d7a309c_aligned.png" # path to source aligned face image
TARGET = r"C:\Users\ru035\Desktop\Icloud\iCloudDrive\Documents\DeepFake_WebDemo\deepfake_site\media\a_53f98b047b194b5f9c7198e98d7a309c.png" # path to target aligned face image or directory
OUTPUT_DIR = "results"                  # directory for swapped results
WEIGHT_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
# =====================

# 將 GitHub Repo 加入模組搜尋路徑 / Add repo to Python path
if os.path.isdir(GITHUB_PROJECT_PATH):
    sys.path.insert(0, GITHUB_PROJECT_PATH)
    print(f"Using MobileFaceSwap code at: {GITHUB_PROJECT_PATH}")
else:
    print(f"警告 Warning: Cannot find MobileFaceSwap at {GITHUB_PROJECT_PATH}")

# Cross-platform image loader
def imread_unicode(path):
    """
    中：跨平台讀取圖片，支援中文與長路徑
    EN：Read images with Unicode/long-path support
    """
    import numpy as _np, cv2 as _cv2
    with open(path, "rb") as f:
        data = f.read()
    arr = _np.frombuffer(data, _np.uint8)
    return _cv2.imdecode(arr, _cv2.IMREAD_COLOR)

if __name__ == "__main__":
    # 僅使用 CPU / CPU only
    paddle.set_device("cpu")
    print("Running on device: cpu")

    # 從 repo 載入 MobileFaceSwap 模型 / init FaceSwap model
    from models.model import FaceSwap, l2_norm
    from models.arcface import IRBlock, ResNet
    from utils.util import cv2paddle, paddle2cv

    model = FaceSwap(False)

    # 載入 ArcFace embedding 網路 / load ArcFace
    id_net = ResNet(block=IRBlock, layers=[3,4,23,3])
    id_net.set_dict(paddle.load(os.path.join(GITHUB_PROJECT_PATH, 'checkpoints', 'arcface.pdparams')))
    id_net.eval()

    # 載入模型權重 / load weights
    weight = paddle.load(WEIGHT_PATH)
    
    # 計算源人臉 embedding / compute source embedding
    src_img = imread_unicode(SOURCE)
    src_img = cv2.resize(src_img, (112,112))
    src_tensor = cv2paddle(src_img)
    mean = paddle.to_tensor([[0.485,0.456,0.406]]).reshape((1,3,1,1))
    std = paddle.to_tensor([[0.229,0.224,0.225]]).reshape((1,3,1,1))
    src_tensor = (src_tensor - mean) / std
    id_emb, id_feat = id_net(src_tensor)
    id_emb = l2_norm(id_emb)

    model.set_model_param(id_emb, id_feat, model_weight=weight)
    model.eval()

    # 確保輸出資料夾存在 / ensure output dir exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 收集目標影像 / gather target images
    if os.path.isfile(TARGET):
        paths = [TARGET]
    else:
        paths = [os.path.join(TARGET, f)
                 for f in os.listdir(TARGET)
                 if f.lower().endswith(('png','jpg','jpeg'))]

    # 執行換臉並保存 / swap and save results
    for tgt in paths:
        img = imread_unicode(tgt)
        # 確保輸入尺寸符合模型期望 / Ensure input size matches model (224x224)
        img_resized = cv2.resize(img, (224, 224))
        tgt_tensor = cv2paddle(img_resized)
        res, _ = model(tgt_tensor)
        out_img = paddle2cv(res)
        base = os.path.splitext(os.path.basename(tgt))[0]
        out_path = os.path.join(OUTPUT_DIR, base + '_swap.png')
        cv2.imwrite(out_path, out_img)
        print(f"Saved swapped image: {out_path}")
