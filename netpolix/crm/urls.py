from django.urls import path
from .views import registro_cliente

urlpatterns = [
    path('registro/', registro_cliente, name='registro_cliente'),  # URL para el registro
    # otras rutas...
]
