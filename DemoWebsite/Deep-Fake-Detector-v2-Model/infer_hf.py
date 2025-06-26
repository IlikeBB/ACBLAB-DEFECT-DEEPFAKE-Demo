# infer_hf.py
import torch
from PIL import Image
from torchvision import transforms
from transformers import AutoImageProcessor, AutoModelForImageClassification

# 1. 指定模型
HF_MODEL = "prithivMLmods/open-deepfake-detection"

# 2. 准备 ImageProcessor（负责 Resize/Crop/Normalize）
processor = AutoImageProcessor.from_pretrained(HF_MODEL)

# 3. 加载模型（会自动下载权重到本地缓存）
model = AutoModelForImageClassification.from_pretrained(HF_MODEL)
model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# 4. 推理函数
def predict(image_path: str):
    # 读图
    img = Image.open(image_path).convert("RGB")
    # 预处理：会自动做 Resize→CenterCrop→ToTensor→Normalize
    inputs = processor(images=img, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**inputs).logits  # shape [1, 2]
        probs  = torch.softmax(logits[0], dim=0).cpu().tolist()
    # 标签映射见 Model Card：id 0 = Realism，1 = Deepfake
    return {"p_real": probs[0], "p_fake": probs[1]}

# 5. 测试
if __name__ == "__main__":
    real_img = "/ssd7/chih/DeepFake_WebDemo/deepfake_site/media/diff_03b91026e9d8442da292b806c75ffbd6.png"
    fake_img = "/ssd7/chih/DeepFake_WebDemo/deepfake_site/media/diff_67912971e8124b6fb6aaa7aab24b32c0.jpg"
    for tag, img in (("真實", real_img), ("偽造", fake_img)):
        out = predict(img)
        label = "偽造" if out["p_fake"] > out["p_real"] else "真實"
        print(f"\n=== {tag} 圖片 ===")
        print(f"P(真實) = {out['p_real']:.4f}")
        print(f"P(偽造) = {out['p_fake']:.4f}")
        print(f"判定  = {label}")
