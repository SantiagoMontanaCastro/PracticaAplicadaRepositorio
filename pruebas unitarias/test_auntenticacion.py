from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Video
from django.http import HttpResponse

class AutenticacionTests(TestCase):

    def setUp(self):
        self.video = Video.objects.create(titulo_original='Video 1', ISAN='123', ano=2020, idioma_original='Español', precio_venta=100, precio_alquiler=10, duracion=90)

    def test_usuario_no_autenticado_redirigido(self):
        response = self.client.get(reverse('catalogo_videos'))
        self.assertRedirects(response, '/login/?next=' + reverse('catalogo_videos'))

        response = self.client.get(reverse('alquilar_venta', args=[self.video.id]))
        self.assertRedirects(response, '/login/?next=' + reverse('alquilar_venta', args=[self.video.id]))

        response = self.client.get(reverse('agregar_al_carrito', args=[self.video.id, 'venta']))
        self.assertRedirects(response, '/login/?next=' + reverse('agregar_al_carrito', args=[self.video.id, 'venta']))