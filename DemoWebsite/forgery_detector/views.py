import os
import uuid
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import FaceSwapForm
from .predict import face_swap

def dashboard(request):
    media_dir    = settings.MEDIA_ROOT
    resource_dir = settings.RESOURCE_ROOT
    fs_media     = FileSystemStorage(location=media_dir,    base_url=settings.MEDIA_URL)
    fs_res       = FileSystemStorage(location=resource_dir, base_url=settings.RESOURCE_URL)

    if request.method == 'GET':
        for key in ('a_name','b_name','swap_name'):
            request.session.pop(key, None)
        for d in (media_dir, resource_dir):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))

    a_name    = request.session.get('a_name')
    b_name    = request.session.get('b_name')
    swap_name = request.session.get('swap_name')

    result_a    = fs_media.url(a_name)   if a_name    else None
    result_b    = fs_media.url(b_name)   if b_name    else None
    result_swap = fs_res.url(swap_name)  if swap_name else None

    form = FaceSwapForm()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'upload':
            form = FaceSwapForm(request.POST, request.FILES)
            if form.is_valid():
                a = form.cleaned_data['src']
                b = form.cleaned_data['dst']
                a_name = f"a_{uuid.uuid4().hex}{os.path.splitext(a.name)[1]}"
                b_name = f"b_{uuid.uuid4().hex}{os.path.splitext(b.name)[1]}"
                fs_media.save(a_name, a)
                fs_media.save(b_name, b)
                request.session['a_name'] = a_name
                request.session['b_name'] = b_name

        elif action == 'swap' and a_name and b_name:
            src_path    = os.path.join(media_dir,    a_name)
            dst_path    = os.path.join(media_dir,    b_name)
            swap_filename = f"swap_{uuid.uuid4().hex}.png"
            swap_path    = os.path.join(resource_dir, swap_filename)
            face_swap(src_path, dst_path, swap_path)
            request.session['swap_name'] = swap_filename

        a_name    = request.session.get('a_name')
        b_name    = request.session.get('b_name')
        swap_name = request.session.get('swap_name')
        result_a    = fs_media.url(a_name)   if a_name    else None
        result_b    = fs_media.url(b_name)   if b_name    else None
        result_swap = fs_res.url(swap_name)  if swap_name else None

    return render(request, 'forgery_detector/dashboard.html', {
        'form':        form,
        'result_a':    result_a,
        'result_b':    result_b,
        'result_swap': result_swap,
    })
