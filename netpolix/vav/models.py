from django.db import models
from crm.models import Perfil
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
 
class Video(models.Model):
    ISAN = models.CharField(max_length=50, unique=True)
    titulo_original = models.CharField(max_length=255)
    ano = models.IntegerField()
    duracion = models.IntegerField()  # en minutos
    calificacion = models.FloatField(default=0.0)
    clasificacion = models.CharField(max_length=10, choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')])
    idioma_original = models.CharField(max_length=50)
    subtitulos = models.CharField(max_length=50, blank=True)
    doblajes = models.CharField(max_length=50, blank=True)
    precio_alquiler = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    poster = models.ImageField(upload_to='posters/') 
    trailer_url = models.URLField(blank=True, null=True)
    full_movie_url = models.URLField(blank=True, null=True)  # URL de la película completa
 
    def __str__(self):
        return self.titulo_original


class AlquilerVenta(models.Model):
    cliente = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[
        ('alquiler', 'Alquiler'), 
        ('venta', 'Venta')
    ])
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    puntos_ganados = models.PositiveIntegerField()  # Cambiado a PositiveIntegerField

    def __str__(self):
        return f"{self.cliente} - {self.video.titulo_original} ({self.tipo})"


def obtener_info_catalogo(self):
        return (f"{self.video.titulo_original} ({self.video.ano}) - {self.video.clasificacion} - "
                f"{self.video.duracion} min - {self.video.calificacion}/10 - "
                f"Precio: ${self.precio}")
        


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    TIPO_CHOICES = [
        ('alquiler', 'Alquiler'),
        ('venta', 'Venta'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField(default=1)  # En caso de que permitas múltiples compras
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.video.titulo_original} - {self.tipo}"
    
    from django.contrib.auth.models import User
from django.db import models

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    purchase_type = models.CharField(max_length=10, choices=[('alquiler', 'Alquiler'), ('venta', 'Venta')])
    payment_status = models.CharField(max_length=15, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.titulo_original} ({self.purchase_type})"

        


