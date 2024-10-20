from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con User
    cedula = models.PositiveIntegerField()  # Número de cédula
    fecha_ingreso = models.DateField()
    referido = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username  # Usamos el username del usuario para identificar el perfil


