from django.db import models
from crm.models import Cliente
from sic.models import Video

# Create your models here.

class AlquilerVenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('alquiler', 'Alquiler'), ('venta', 'Venta')])
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    puntos_ganados = models.IntegerField()
    
    def __str__(self):
        return f"{self.cliente} - {self.video.titulo_original} ({self.tipo})"

