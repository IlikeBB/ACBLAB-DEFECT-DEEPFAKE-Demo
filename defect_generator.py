# defect_generator_debug.py
import os, sys, cv2, numpy as np, paddle

# === CONFIGURATION ===
dir_here = os.path.dirname(os.path.abspath(__file__))
GITHUB_PROJECT_PATH = os.path.join(dir_here, "MobileFaceSwap")
SOURCE = "./Demo_Image/073_032.png"
TARGET = "./Demo_Image/000_098.png"
OUTPUT_DIR = "results"
# 權重路徑
ARC_PATH = os.path.join(GITHUB_PROJECT_PATH, 'checkpoints', 'arcface.pdparams')
MFSWAP_PATH = os.path.join(GITHUB_PROJECT_PATH, "checkpoints", "MobileFaceSwap_224.pdparams")
# =====================

# 加入模組路徑
if os.path.isdir(GITHUB_PROJECT_PATH):
    sys.path.insert(0, GITHUB_PROJECT_PATH)
    print("Using MobileFaceSwap code at:", GITHUB_PROJECT_PATH)
else:
    raise FileNotFoundError(f"找不到 MobileFaceSwap Repo: {GITHUB_PROJECT_PATH}")

# 讀影像函式
def imread_unicode(path):
    with open(path, "rb") as f:
        data = f.read()
    arr = np.frombuffer(data, np.uint8)
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)

if __name__ == "__main__":
    paddle.set_device("cpu")
    print("Running on device:", paddle.get_device())

    # 載入模型
    from models.model import FaceSwap, l2_norm
    from models.arcface import IRBlock, ResNet
    from utils.util import cv2paddle, paddle2cv

    # 1. ArcFace encoding network
    id_net = ResNet(block=IRBlock, layers=[3,4,23,3])
    print("Loading ArcFace weights:", ARC_PATH)
    id_state = paddle.load(ARC_PATH)
    id_net.set_state_dict(id_state)       # ← 改用 set_state_dict
    id_net.eval()

    # 2. FaceSwap network
    model = FaceSwap(use_gpu=False)       # 確認 API 參數
    print("Loading FaceSwap weights:", MFSWAP_PATH)
    fs_state = paddle.load(MFSWAP_PATH)
    model.set_model_param(None, None, model_weight=fs_state)
    model.eval()

    # 計算 source embedding
    src_img = imread_unicode(SOURCE)
    src_img = cv2.resize(src_img, (112,112))
    src_t = cv2paddle(src_img)
    src_t = src_t.unsqueeze(0)            # 加 batch 維度
    mean = paddle.to_tensor([0.485,0.456,0.406]).reshape((1,3,1,1))
    std  = paddle.to_tensor([0.229,0.224,0.225]).reshape((1,3,1,1))
    src_t = (src_t - mean) / std
    with paddle.no_grad():
        id_emb, id_feat = id_net(src_t)
    id_emb = l2_norm(id_emb)

    # 更新到 FaceSwap
    model.set_model_param(id_emb, id_feat, model_weight=None)

    # 確保 output 目錄
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 處理目標
    tgt_paths = [TARGET] if os.path.isfile(TARGET) else [
        os.path.join(TARGET, f) for f in os.listdir(TARGET)
        if f.lower().endswith(('.png','jpg','jpeg'))
    ]

    for tgt in tgt_paths:
        print("Processing:", tgt)
        img = imread_unicode(tgt)
        img224 = cv2.resize(img, (224,224))
        tgt_t = cv2paddle(img224).unsqueeze(0)
        tgt_t = (tgt_t - mean) / std

        with paddle.no_grad():
            res, _ = model(tgt_t)           # 推論
        out = paddle2cv(res[0])             # 取 batch[0]
        # 保證值域
        out = np.clip(out, 0, 255).astype(np.uint8)

        name = os.path.splitext(os.path.basename(tgt))[0]
        out_path = os.path.join(OUTPUT_DIR, name + '_swap.png')
        cv2.imwrite(out_path, out)
        print("Saved:", out_path)
