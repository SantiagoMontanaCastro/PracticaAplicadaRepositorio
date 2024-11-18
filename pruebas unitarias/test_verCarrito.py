from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Carrito, Video
from django.http import HttpResponse
from django.contrib.messages import get_messages

class VerCarritoTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.video1 = Video.objects.create(titulo_original='Video 1', ISAN='123', ano=2020, idioma_original='Español', precio_venta=100, precio_alquiler=10, duracion=120)
        self.video2 = Video.objects.create(titulo_original='Video 2', ISAN='456', ano=2021, idioma_original='Inglés', precio_venta=150, precio_alquiler=15,  duracion=90)

    def test_ver_carrito_con_video(self):
        self.client.login(username='testuser', password='password')
        # Agregar videos al carrito
        self.client.get(reverse('agregar_al_carrito', args=[self.video1.id, 'venta']))
        self.client.get(reverse('agregar_al_carrito', args=[self.video2.id, 'alquiler']))

        response = self.client.get(reverse('ver_carrito'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Video 1')
        self.assertContains(response, 'Video 2')
        self.assertContains(response, 'Total: 115') 