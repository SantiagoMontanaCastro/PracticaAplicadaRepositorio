from django.urls import path
from .views import catalogo_videos, alquilar_venta, agregar_al_carrito, pagina_inicio,ver_carrito,logout_view


urlpatterns = [
    path('', pagina_inicio, name='home'),  # URL para la página de inicio
    path('catalogo/', catalogo_videos, name='catalogo_videos'),
    path('alquilar_venta/<int:video_id>/', alquilar_venta, name='alquilar_venta'),  # Ruta para alquilar/venta
    path('agregar_al_carrito/<int:video_id>/<str:tipo>/', agregar_al_carrito, name='agregar_al_carrito'), # Ruta para agregar al carrito
    path('carrito/', ver_carrito, name='ver_carrito'),# Ruta para ver el carrito
    path('logout/', logout_view, name='logout'),
]

