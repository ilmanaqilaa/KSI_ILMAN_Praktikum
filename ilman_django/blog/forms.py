from django import forms

class nameclass(forms.Form):
    nama = forms.CharField()

class classforms(forms.Form):
    namac = forms.CharField()
    alamatc = forms.CharField()