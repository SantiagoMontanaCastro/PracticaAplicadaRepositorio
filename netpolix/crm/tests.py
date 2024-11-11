# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import RegistroClienteForm
from .models import Perfil
from datetime import date

class RegistroClienteFormTest(TestCase):
    def test_form_valido(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
            'cedula': 123456789,
            'fecha_ingreso': '2023-11-11'
        }
        form = RegistroClienteForm(data=data)
        self.assertTrue(form.is_valid(), "El formulario debería ser válido con datos correctos")
        print("Formulario válido con datos correctos.")

    def test_creacion_usuario_y_perfil(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
            'cedula': 123456789,
            'fecha_ingreso': '2023-11-11'
        }
        form = RegistroClienteForm(data=data)
        
        self.assertTrue(form.is_valid(), "El formulario debería ser válido con datos correctos")
        print("Formulario válido. Procediendo a guardar el usuario y perfil.")

        user = form.save()
        
        self.assertIsNotNone(user, "El usuario debería ser creado")
        print(f"Usuario '{user.username}' creado exitosamente.")

        perfil = Perfil.objects.get(user=user)
        self.assertEqual(perfil.cedula, data['cedula'], "La cédula del perfil debería coincidir")
        self.assertEqual(perfil.fecha_ingreso, date(2023, 11, 11), "La fecha de ingreso debería coincidir")
        print("Perfil creado exitosamente con los datos correctos (cédula y fecha de ingreso).")

    def test_form_invalido_sin_cedula(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
            'fecha_ingreso': '2023-11-11'
        }
        form = RegistroClienteForm(data=data)
        self.assertFalse(form.is_valid(), "El formulario debería ser inválido sin cédula")
        self.assertIn('cedula', form.errors, "El formulario debería tener un error en el campo cedula")
        print("Formulario inválido al faltar el campo cédula. Error en cedula detectado correctamente.")
