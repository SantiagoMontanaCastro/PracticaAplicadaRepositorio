from django.db import models

# Create your models here.

nombre = models.CharField(max_length=100)
descripcion = models.TextField()
calificacion = models.FloatField(default=0)


def __str__(self):
   return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra de {self.usuario} por {self.monto}'
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra de {self.usuario} por {self.monto}'