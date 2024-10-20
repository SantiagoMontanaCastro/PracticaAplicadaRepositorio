from django import forms

class VideoSearchForm(forms.Form):
    ISAN = forms.CharField(max_length=50, required=False, label='ISAN')
    titulo_original = forms.CharField(max_length=255, required=False, label='Título')
    ano = forms.IntegerField(required=False, label='Año')
    idioma_original = forms.CharField(max_length=50, required=False, label='Idioma')
