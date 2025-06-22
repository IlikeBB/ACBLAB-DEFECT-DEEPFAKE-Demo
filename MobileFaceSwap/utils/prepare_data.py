import os
import glob
import os.path as osp
import inspect
import numpy as np
from insightface.model_zoo import model_zoo

class LandmarkModel:
    def __init__(self, name, root='./checkpoints'):
        self.models = {}
        root = os.path.expanduser(root)
        onnx_files = glob.glob(osp.join(root, name, '*.onnx'))
        onnx_files = sorted(onnx_files)
        for onnx_file in onnx_files:
            if '_selfgen_' in onnx_file:
                continue
            model = model_zoo.get_model(onnx_file)
            task = model.taskname
            if task not in self.models:
                print('find model:', onnx_file, task)
                self.models[task] = model
            else:
                print('duplicated model task type, ignore:', onnx_file, task)
                del model
        assert 'detection' in self.models, 'Detection model not found'
        self.det_model = self.models['detection']

    def prepare(self, ctx_id, det_thresh=0.5, det_size=(640, 640), mode='None'):
        self.det_thresh = det_thresh
        self.det_size = det_size
        self.mode = mode
        print('set det-size:', det_size)
        for task, model in self.models.items():
            if task == 'detection':
                model.prepare(ctx_id, input_size=det_size)
            else:
                model.prepare(ctx_id)

    def get(self, img, max_num=0):
        # Dynamically adapt to detect() signature
        sig = inspect.signature(self.det_model.detect)
        params = sig.parameters
        args = [img]
        kwargs = {}
        if 'input_size' in params:
            args.append(self.det_size)
        if 'threshold' in params:
            kwargs['threshold'] = self.det_thresh
        if 'score_thresh' in params:
            kwargs['score_thresh'] = self.det_thresh
        if 'max_num' in params:
            kwargs['max_num'] = max_num
        if 'metric' in params:
            kwargs['metric'] = 'default'

        bboxes, kpss = self.det_model.detect(*args, **kwargs)
        if bboxes is None or bboxes.shape[0] == 0:
            return None
        det_score = bboxes[..., 4]
        best_index = int(np.argmax(det_score))
        return None if kpss is None else kpss[best_index]

    def gets(self, img, max_num=0):
        # Return all keypoints
        sig = inspect.signature(self.det_model.detect)
        params = sig.parameters
        args = [img]
        kwargs = {}
        if 'input_size' in params:
            args.append(self.det_size)
        if 'threshold' in params:
            kwargs['threshold'] = self.det_thresh
        if 'score_thresh' in params:
            kwargs['score_thresh'] = self.det_thresh
        if 'max_num' in params:
            kwargs['max_num'] = max_num
        if 'metric' in params:
            kwargs['metric'] = 'default'
        _, kpss = self.det_model.detect(*args, **kwargs)
        return kpss
