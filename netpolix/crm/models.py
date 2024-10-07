from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    cedula = models.PositiveIntegerField()  # Permite números entre 0 y 2,147,483,647
    fecha_ingreso = models.DateField()
    referido = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    puntos = models.IntegerField(default=0)
    
    def __str__(self):
     return self.nombre


