from django import forms

from django.conf import settings
class FaceSwapForm(forms.Form):
    src = forms.ImageField(label="來源圖片 A")
    dst = forms.ImageField(label="目標圖片 B")

class DiffDetectForm(forms.Form):
    diff_img = forms.ImageField(label='選擇檢測圖片')
    model_choice = forms.ChoiceField(
        choices=settings.DETECT_MODEL_CHOICES,
        initial=settings.DEFAULT_DETECT_MODEL,
        label='選擇檢測模型'
    )
