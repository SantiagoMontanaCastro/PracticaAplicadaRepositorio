from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Carrito, Video
from django.http import HttpResponse
from django.contrib.messages import get_messages

class AgregarAlCarritoTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.video = Video.objects.create(titulo_original='Video 1', ISAN='123', ano=2020, idioma_original='Español', precio_venta=100, precio_alquiler=10,  duracion=90)

    def test_agregar_al_carrito(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('agregar_al_carrito', args=[self.video.id, 'venta']))
        self.assertRedirects(response, reverse('ver_carrito'))

        # Verificar que el video fue agregado al carrito
        from .models import Carrito
        carrito_item = Carrito.objects.filter(usuario=self.user, video=self.video, tipo='venta').first()
        self.assertIsNotNone(carrito_item)

    def test_agregar_video_ya_en_carrito(self):
        self.client.login(username='testuser', password='password')
        self.client.get(reverse('agregar_al_carrito', args=[self.video.id, 'venta']))

        # Intentar agregar el mismo video de nuevo
        response = self.client.get(reverse('agregar_al_carrito', args=[self.video.id, 'venta']))
        self.assertContains(response, "El video 'Video 1' ya está en tu carrito como venta.")

        # Verificar que solo hay un item en el carrito
        carrito_items = Carrito.objects.filter(usuario=self.user, video=self.video, tipo='venta')
        self.assertEqual(carrito_items.count(), 1)