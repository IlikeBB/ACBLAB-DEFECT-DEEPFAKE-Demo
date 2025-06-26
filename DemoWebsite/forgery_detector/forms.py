from django import forms

class FaceSwapForm(forms.Form):
    src = forms.ImageField(label="來源圖片 A")
    dst = forms.ImageField(label="目標圖片 B")
