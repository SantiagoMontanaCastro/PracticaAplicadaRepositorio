# vav/urls.py

from django.urls import path
from .views import catalogo_videos, alquilar_venta

urlpatterns = [
    path('catalogo/', catalogo_videos, name='catalogo_videos'),
    path('alquilar_venta/<int:video_id>/', alquilar_venta, name='alquilar_venta'),  # Ruta para alquilar/venta
]
