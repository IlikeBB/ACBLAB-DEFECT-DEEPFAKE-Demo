# defect_detector_hf.py
"""
Transformer-based Deepfake Detection Script (Single Image, CPU Only)
使用 HuggingFace Transformers 模型檢測單張圖像是否偽造 / Detect a single deepfake image with HF Transformers

1. 修改 IMAGE_PATH 變數為你的圖像路徑
2. 執行：python defect_detector_hf.py
"""
import os
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

def predict(image_path: str):
    """
    中：讀取並轉換為 RGB 圖像 / EN: load as RGB image
    """
    img = Image.open(image_path).convert("RGB")
    inputs = processor(images=img, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits  # [1,2]
        probs = torch.softmax(logits[0], dim=0).cpu().tolist()
    # id 0 = Real, 1 = Deepfake
    return {"p_real": probs[0], "p_fake": probs[1]}

if __name__ == '__main__':
    
    # === CONFIGURATION ===
    # 僅需指定單張圖像路徑 / Specify a single image path
    IMAGE_PATH = r"C:\Users\ru035\Desktop\Icloud\iCloudDrive\Documents\DeepFake_WebDemo\results\a_53f98b047b194b5f9c7198e98d7a309c_swap.png"  # 中/EN: Path to the image file to test
    # 使用的 HuggingFace 模型 ID / HF_MODEL: Pretrained model identifier
    HF_MODEL = "prithivMLmods/open-deepfake-detection"
    # =====================

    # Initialize processor and model (CPU only)
    processor = AutoImageProcessor.from_pretrained(HF_MODEL)
    model = AutoModelForImageClassification.from_pretrained(HF_MODEL)
    model.eval()

    # Always use CPU
    device = torch.device('cpu')
    print(f"Using device: {device}")
    
    
    # 只對單張圖片進行檢測 / Single-image detection
    if not os.path.isfile(IMAGE_PATH):
        raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")
    # 執行預測 / perform prediction
    scores = predict(IMAGE_PATH)
    label = "偽造 Deepfake" if scores["p_fake"] > scores["p_real"] else "真實 Real"
    print(f"\n=== Image: {IMAGE_PATH} ===")
    print(f"P(Real)= {scores['p_real']:.4f}")
    print(f"P(Deepfake)= {scores['p_fake']:.4f}")
    print(f"判定 Label: {label}")
