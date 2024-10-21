from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Compra, Usuario

@receiver(post_save, sender=Compra)
def agregar_puntos(sender, instance, created, **kwargs):
    if created:
        # Sumar 1 punto por cada compra realizada
        usuario = instance.usuario
        usuario.puntos += 1
        usuario.save()