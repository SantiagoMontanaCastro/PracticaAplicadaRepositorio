from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Video
from django.http import HttpResponse

class AlquilarVentaTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.video = Video.objects.create(titulo_original='Video 1', ISAN='123', ano=2020, idioma_original='Español', precio_venta=100, precio_alquiler=10,  duracion=90)

    def test_alquilar_venta_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('alquilar_venta', args=[self.video.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Video 1')
    
    def test_alquilar_venta_unauthenticated_user(self):
        response = self.client.get(reverse('alquilar_venta', args=[self.video.id]))
        self.assertRedirects(response, '/login/?next=' + reverse('alquilar_venta', args=[self.video.id])) 