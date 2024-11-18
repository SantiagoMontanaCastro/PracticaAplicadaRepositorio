from django.test import TestCase
from django.contrib.auth.models import User
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
