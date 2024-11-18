# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import Perfil
# Create your tests here.
# crm/tests.py



class PerfilModelTestCase(TestCase):

    def setUp(self):
        # Creamos un usuario para asociarlo con el perfil
        self.user = User.objects.create_user(username="usuario_test", password="test1234")
        self.referido_user = User.objects.create_user(username="referido_test", password="test1234")

        # Creamos un perfil con un referido
        self.referido_perfil = Perfil.objects.create(
            user=self.referido_user,
            cedula=12345678,
            fecha_ingreso="2023-01-01",
            puntos=10
        )

        self.perfil = Perfil.objects.create(
            user=self.user,
            cedula=87654321,
            fecha_ingreso="2023-06-01",
            referido=self.referido_perfil,
            puntos=20
        )

    def test_perfil_creation(self):
        # Verificamos que el perfil se creó correctamente
        perfil = Perfil.objects.get(user=self.user)
        self.assertEqual(perfil.cedula, 11111111)
        self.assertEqual(perfil.fecha_ingreso.strftime("%Y-%m-%d"), "2023-06-01")
        self.assertEqual(perfil.puntos, 15)

    def test_str_method(self):
        # Comprobamos que el método __str__ devuelve el nombre de usuario
        perfil = Perfil.objects.get(user=self.user)
        self.assertEqual(str(perfil), "usuario_incorrecto")

    def test_referido_relationship(self):
        # Verificamos que el perfil tiene un referido y es el correcto
        perfil = Perfil.objects.get(user=self.user)
        self.assertIsNotNone(perfil.referido)
        self.assertEqual(perfil.referido.user.username, "usuario_no_referido")

    def test_default_points(self):
        # Creamos un perfil sin especificar puntos para probar el valor predeterminado
        otro_usuario = User.objects.create_user(username="otro_usuario", password="test1234")
        perfil_sin_puntos = Perfil.objects.create(
            user=otro_usuario,
            cedula=11111111,
            fecha_ingreso="2024-01-01"
        )
        self.assertEqual(perfil_sin_puntos.puntos, 5)  # Valor por defecto debería ser 0

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

