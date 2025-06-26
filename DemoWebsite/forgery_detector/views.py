# forgery_detector/views.py
import os
import uuid
import torch
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import FaceSwapForm, DiffDetectForm
from .detector import detect_deepfake

def dashboard(request):
    # 1. 設定檔案儲存目錄
    media_dir    = settings.MEDIA_ROOT
    resource_dir = settings.RESOURCE_ROOT
    fs_media     = FileSystemStorage(location=media_dir,    base_url=settings.MEDIA_URL)
    fs_res       = FileSystemStorage(location=resource_dir, base_url=settings.RESOURCE_URL)

    # 2. 處理 GET：清空 session 與資料夾內容
    if request.method == 'GET':
        for key in ('a_name', 'b_name', 'swap_name', 'swap_error', 'diff_src', 'diff_result', 'diff_model'):
            request.session.pop(key, None)
        for d in (media_dir, resource_dir):
            for f in os.listdir(d):
                try:
                    os.remove(os.path.join(d, f))
                except:
                    pass

    # 3. 從 session 讀取先前結果
    result_a    = fs_media.url(request.session.get('a_name'))   if request.session.get('a_name')   else None
    result_b    = fs_media.url(request.session.get('b_name'))   if request.session.get('b_name')   else None
    result_swap = fs_res.url(request.session.get('swap_name'))  if request.session.get('swap_name') else None
    swap_error  = request.session.get('swap_error')
    diff_src    = request.session.get('diff_src')
    diff_result = request.session.get('diff_result')
    diff_model  = request.session.get('diff_model', settings.DEFAULT_DETECT_MODEL)

    # 4. 初始化表單
    swap_form = FaceSwapForm(request.POST or None, request.FILES or None)
    diff_form = DiffDetectForm(request.POST or None, request.FILES or None)

    # 5. 處理 POST
    if request.method == 'POST':
        action = request.POST.get('action')

        # 5.1 上傳 A/B
        if action == 'upload' and swap_form.is_valid():
            src = swap_form.cleaned_data['src']
            a_name = f"a_{uuid.uuid4().hex}{os.path.splitext(src.name)[1]}"
            fs_media.save(a_name, src)
            request.session['a_name'] = a_name

            dst = swap_form.cleaned_data['dst']
            b_name = f"b_{uuid.uuid4().hex}{os.path.splitext(dst.name)[1]}"
            fs_media.save(b_name, dst)
            request.session['b_name'] = b_name

        # 5.2 執行換臉
        elif action == 'swap' and request.session.get('a_name') and request.session.get('b_name'):
            src_path = os.path.join(media_dir, request.session['a_name'])
            dst_path = os.path.join(media_dir, request.session['b_name'])
            out_filename = request.session['b_name']
            out_path = os.path.join(resource_dir, out_filename)

            from .predict import face_swap
            try:
                face_swap(src_path, dst_path, out_path)
            except Exception as e:
                request.session['swap_error'] = str(e)

            # 如果預期檔案不存在，掃描 resource_dir 找最新檔
            if not os.path.isfile(out_path):
                imgs = [f for f in os.listdir(resource_dir)
                        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
                if imgs:
                    latest = max(
                        imgs,
                        key=lambda fn: os.path.getmtime(os.path.join(resource_dir, fn))
                    )
                    out_filename = latest
                    out_path = os.path.join(resource_dir, out_filename)
                else:
                    request.session['swap_error'] = "Resource 資料夾中找不到任何圖檔"

            request.session['swap_name']  = out_filename

        # 5.3 圖片真偽檢測
        elif action == 'detect' and diff_form.is_valid():
            diff_file    = diff_form.cleaned_data['diff_img']
            model_choice = diff_form.cleaned_data['model_choice']

            diff_name = f"diff_{uuid.uuid4().hex}{os.path.splitext(diff_file.name)[1]}"
            fs_media.save(diff_name, diff_file)
            diff_src = fs_media.url(diff_name)
            request.session['diff_src'] = diff_src
            diff_path = os.path.join(media_dir, diff_name)

            out = detect_deepfake(diff_path, model_choice)
            request.session['diff_result'] = out
            request.session['diff_model']  = model_choice

        # 5.4 更新 session 讀取
        result_a    = fs_media.url(request.session.get('a_name'))   if request.session.get('a_name')   else None
        result_b    = fs_media.url(request.session.get('b_name'))   if request.session.get('b_name')   else None
        result_swap = fs_res.url(request.session.get('swap_name'))  if request.session.get('swap_name') else None
        swap_error  = request.session.get('swap_error')
        diff_src    = request.session.get('diff_src')
        diff_result = request.session.get('diff_result')
        diff_model  = request.session.get('diff_model', settings.DEFAULT_DETECT_MODEL)

    return render(request, 'forgery_detector/dashboard.html', {
        'swap_form':   swap_form,
        'diff_form':   diff_form,
        'result_a':    result_a,
        'result_b':    result_b,
        'result_swap': result_swap,
        'diff_src':    diff_src,
        'diff_result': diff_result,
        'diff_model':  dict(settings.DETECT_MODEL_CHOICES).get(diff_model, diff_model),
        'swap_model_link':   'https://github.com/Seanseattle/MobileFaceSwap',
        'detect_model_link': 'https://huggingface.co/models?sort=downloads&search=deepfake',
    })
