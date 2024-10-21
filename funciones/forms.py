from django import forms
from .models import Compra


query = forms.CharField(label='Buscar', max_length=100)

class CalificacionForm(forms.Form):
    estrellas = forms.ChoiceField(choices=[
        (1, '1 estrella'),
        (2, '2 estrellas'),
        (3, '3 estrellas'),
        (4, '4 estrellas'),
        (5, '5 estrellas')
    ])



class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['monto']



class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['monto']