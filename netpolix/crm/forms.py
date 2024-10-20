from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroClienteForm(UserCreationForm):
    cedula = forms.IntegerField(required=True)
    fecha_ingreso = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'cedula', 'fecha_ingreso']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear el perfil del cliente
            Perfil.objects.create(
                user=user,
                cedula=self.cleaned_data['cedula'],
                fecha_ingreso=self.cleaned_data['fecha_ingreso']
            )
        return user
