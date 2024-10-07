from django.db import models

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
    
    def __str__(self):
        return self.titulo_original


