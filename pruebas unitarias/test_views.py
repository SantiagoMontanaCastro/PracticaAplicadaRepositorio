from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from vav.models import Video

class CatalogoVideosTestCase(TestCase):
    
    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(username='testandres', password='contraseña')

        # Crear algunos videos de prueba en la base de datos
        self.video1 = Video.objects.create(
            ISAN="564",
            titulo_original="Titanic",
            ano=1999,
            duracion=195,  # Duración en minutos
            calificacion=8.0,
            clasificacion="PG-13",
            idioma_original="ingles",
            subtitulos="español",
            doblajes="no",
            precio_alquiler=9.99,
            precio_venta=20.2,
            poster="posters/Titanic.jpg"
        )
        self.video2 = Video.objects.create(
            ISAN="231323",
            titulo_original="Rampage",
            ano=2018,
            duracion=117,
            calificacion=4.8,
            clasificacion="PG-13",
            idioma_original="Español",
            subtitulos="Inglés",
            doblajes="Aleman",
            precio_alquiler=5.99,
            precio_venta=8.97,
            poster="posters/MV5BNDA1NjA3ODU3OV5BMl5BanBnXkFtZTgwOTg3MTIwNTM._V1_FMjpg_UX1000_.jpg"
        )

    def test_busqueda_por_ISAN(self):
        # Hacer login del usuario
        self.client.login(username='testuser', password='password123')

        url = reverse('catalogo_videos')  # URL de la vista 'catalogo_videos'
        response = self.client.get(url, {'ISAN': '564'})  # Filtrar por ISAN
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Titanic")
        self.assertNotContains(response, "Rampage")
    
    def test_busqueda_por_titulo(self):
        # Hacer login del usuario
        self.client.login(username='testuser', password='password123')

        url = reverse('catalogo_videos')  # URL de la vista 'catalogo_videos'
        response = self.client.get(url, {'titulo_original': 'Rampage'})  # Filtrar por título
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rampage")
        self.assertNotContains(response, "Titanic")
    
    def test_busqueda_por_ano(self):
        # Hacer login del usuario
        self.client.login(username='testuser', password='password123')

        url = reverse('catalogo_videos')  # URL de la vista 'catalogo_videos'
        response = self.client.get(url, {'ano': 1999})  # Filtrar por año
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Titanic")
        self.assertNotContains(response, "Rampage")
    
    def test_busqueda_por_idioma(self):
        # Hacer login del usuario
        self.client.login(username='testuser', password='password123')

        url = reverse('catalogo_videos')  # URL de la vista 'catalogo_videos'
        response = self.client.get(url, {'idioma_original': 'ingles'})  # Filtrar por idioma
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Titanic")
        self.assertNotContains(response, "Rampage")
    
    def test_formulario_invalido(self):
        # Hacer login del usuario
        self.client.login(username='testuser', password='password123')

        url = reverse('catalogo_videos')
        response = self.client.get(url, {'ISAN': 'invalidisan'})  # Filtrar por un ISAN inválido
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Titanic")
        self.assertNotContains(response, "Rampage")