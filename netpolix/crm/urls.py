from django.urls import path
from .views import registro_cliente, ingreso_usuario
urlpatterns = [
    path('registro/', registro_cliente, name='registro_cliente'),
    path('login/',ingreso_usuario),   # URL para el registro
    # otras rutas...
]
