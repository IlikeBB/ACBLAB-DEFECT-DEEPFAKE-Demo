import os, torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

# 模型快取
_loaded_models = {}

# 支援模型選項
MODEL_MAP = {
    'hf_vit':      'prithivMLmods/Deep-Fake-Detector-v2-Model',
    'Wvolf':       'Wvolf/ViT_Deepfake_Detection',
    'HrutikAdsare':'HrutikAdsare/deepfake-detector-faceforensics',
    'dima806':     'dima806/deepfake_vs_real_image_detection',
    # 'mesonet':  # 可擴充
}

def detect_deepfake(image_path: str, model_name: str = 'hf_vit') -> dict:
    """
    對單張圖做 deepfake 偵測
    Params:
        image_path: 圖片路徑
        model_name: MODEL_MAP 的 key
    Returns:
        dict 包含 'p_real', 'p_fake', 'label'
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"找不到檔案：{image_path}")
    
    # 模型載入與快取
    if model_name not in _loaded_models:
        if model_name not in MODEL_MAP:
            raise ValueError(f"未知模型名稱：{model_name}")
        hf_name = MODEL_MAP[model_name]
        processor = AutoImageProcessor.from_pretrained(hf_name)
        model = AutoModelForImageClassification.from_pretrained(
            hf_name,
            trust_remote_code=True,
            use_safetensors=True
        ).to('cuda' if torch.cuda.is_available() else 'cpu')
        model.eval()
        _loaded_models[model_name] = (processor, model)

    processor, model = _loaded_models[model_name]

    # 圖像預處理與推論
    img = Image.open(image_path).convert('RGB')
    inputs = processor(images=img, return_tensors='pt').to(model.device)

    with torch.no_grad():
        logits = model(**inputs).logits[0]
        probs = torch.softmax(logits, dim=0).cpu().tolist()
    
    # Label 解釋（假設 [0]=real, [1]=fake）
    label = 'Fake!!' if probs[1] > probs[0] else 'Real!!'
    return {
        'p_real': round(probs[0], 4),
        'p_fake': round(probs[1], 4),
        'label': label
    }
