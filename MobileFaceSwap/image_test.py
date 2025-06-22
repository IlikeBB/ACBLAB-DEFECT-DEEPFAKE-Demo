import os
import sys
import types
# Prevent insightface.app from loading albumentations and torch
sys.modules['insightface.app'] = types.ModuleType('insightface.app')
sys.modules['insightface.app.mask_renderer'] = types.ModuleType('insightface.app.mask_renderer')

import paddle
import argparse
import numpy as np
import cv2
import subprocess
from models.model import FaceSwap, l2_norm
from models.arcface import IRBlock, ResNet
from utils.align_face import back_matrix, dealign, align_img
from utils.util import paddle2cv, cv2paddle
from utils.prepare_data import LandmarkModel

# Ensure UTF-8 mode for subprocess child processes
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["PYTHONUTF8"] = "1"
# Force first GPU only
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Cross-platform image loader to handle unicode/long paths

def imread_unicode(path):
    import numpy as _np, cv2 as _cv2
    with open(path, 'rb') as f:
        data = f.read()
    arr = _np.frombuffer(data, _np.uint8)
    img = _cv2.imdecode(arr, _cv2.IMREAD_COLOR)
    return img


def get_id_emb(id_net, id_img_path):
    # Use unicode-safe loader
    id_img = imread_unicode(id_img_path)
    id_img = cv2.resize(id_img, (112, 112))
    id_img = cv2paddle(id_img)
    mean = paddle.to_tensor([[0.485, 0.456, 0.406]]).reshape((1, 3, 1, 1))
    std = paddle.to_tensor([[0.229, 0.224, 0.225]]).reshape((1, 3, 1, 1))
    id_img = (id_img - mean) / std

    id_emb, id_feature = id_net(id_img)
    id_emb = l2_norm(id_emb)
    return id_emb, id_feature


def image_test(args):
    # 动态判断是否支持 GPU
    use_gpu = args.use_gpu and paddle.is_compiled_with_cuda()
    if args.use_gpu and not use_gpu:
        print(">> [image_test] 警告：請求使用 GPU，但當前 PaddlePaddle 不是以 CUDA 編譯，將使用 CPU 模式。")
    # 设置 Paddle 设备，优先 GPU
    paddle.set_device("gpu:0" if use_gpu else "cpu")
    # 初始化人脸互换模型
    faceswap_model = FaceSwap(use_gpu)

    # ArcFace 识别网络
    id_net = ResNet(block=IRBlock, layers=[3, 4, 23, 3])
    id_net.set_dict(paddle.load('./checkpoints/arcface.pdparams'))
    id_net.eval()

    # 加载 SimSwap 权重
    weight = paddle.load('./checkpoints/MobileFaceSwap_224.pdparams')
    print("weight loading finish!!!!!")

    # 获取经过对齐的源人脸 embedding
    base_path = args.source_img_path.rsplit('.', 1)[0]
    aligned_path = base_path + '_aligned.png'
    id_emb, id_feature = get_id_emb(id_net, aligned_path)

    faceswap_model.set_model_param(id_emb, id_feature, model_weight=weight)
    faceswap_model.eval()

    # 准备目标图像列表
    if os.path.isfile(args.target_img_path):
        img_list = [args.target_img_path]
    else:
        img_list = [os.path.join(args.target_img_path, x)
                    for x in os.listdir(args.target_img_path)
                    if x.lower().endswith(('png','jpg','jpeg'))]

    # 逐张处理
    for img_path in img_list:
        origin_att_img = imread_unicode(img_path)
        aligned_att_path = img_path.rsplit('.', 1)[0] + '_aligned.png'
        att_img = imread_unicode(aligned_att_path)
        att_img = cv2paddle(att_img)
        
        res, mask = faceswap_model(att_img)
        res = paddle2cv(res)
        print(f">> [image_test] Model output shape: {res.shape}")

        if args.merge_result:
            back = np.load(aligned_att_path.rsplit('_aligned.png', 1)[0] + '_back.npy')
            mask = np.transpose(mask[0].numpy(), (1, 2, 0))
            res = dealign(res, origin_att_img, back, mask)

        out_file = os.path.join(args.output_dir, os.path.basename(img_path))
        cv2.imwrite(out_file, res)


def face_align(landmarkModel, image_path, merge_result=False, image_size=224):
    if os.path.isfile(image_path):
        img_list = [image_path]
    else:
        img_list = [os.path.join(image_path, x)
                    for x in os.listdir(image_path)
                    if x.lower().endswith(('png','jpg','jpeg'))]

    for path in img_list:
        img = imread_unicode(path)
        landmark = landmarkModel.get(img)
        if landmark is not None:
            base = path.rsplit('.', 1)[0]
            aligned_img, back = align_img(img, landmark, image_size)
            cv2.imwrite(base + '_aligned.png', aligned_img)
            if merge_result:
                np.save(base + '_back.npy', back)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MobileFaceSwap Test")
    parser.add_argument('--source_img_path', type=str, help='path to the source image')
    parser.add_argument('--target_img_path', type=str, help='path to the target images')
    parser.add_argument('--output_dir', type=str, default='results', help='path to output dirs')
    parser.add_argument('--image_size', type=int, default=224,
                        help='size of test images (224 SimSwap | 256 FaceShifter)')
    parser.add_argument('--merge_result', type=bool, default=True,
                        help='output with whole image')
    parser.add_argument('--need_align', type=bool, default=True,
                        help='need to align images')
    parser.add_argument('--use_gpu', type=bool, default=False)

    args = parser.parse_args()
    if args.need_align:
        landmarkModel = LandmarkModel(name='landmarks')
        landmarkModel.prepare(ctx_id=0, det_thresh=0.6, det_size=(640, 640))
        face_align(landmarkModel, args.source_img_path, args.merge_result, args.image_size)
        face_align(landmarkModel, args.target_img_path, args.merge_result, args.image_size)

    os.makedirs(args.output_dir, exist_ok=True)
    image_test(args)
