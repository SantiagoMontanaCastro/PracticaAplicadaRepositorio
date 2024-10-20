from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Video
from .carrito import Carrito  # Importamos la clase Carrito
from .models import AlquilerVenta
# Create your views here.



def catalogo_videos(request):
    # Obtener todos los videos de la base de datos
    videos = Video.objects.all()
    
    # Renderizar la plantilla y pasar la lista de videos
    return render(request, 'vav/catalogo.html', {'videos': videos})


def alquilar_venta(request, video_id):
    # Obtiene el video correspondiente por su ID
    video = get_object_or_404(Video, id=video_id)

    # Aquí puedes agregar la lógica para manejar el alquiler o la venta
    # Por ejemplo, puedes crear un nuevo objeto AlquilerVenta si es necesario

    return render(request, 'vav/alquilar_venta.html', {'video': video})


def pagina_inicio(request):

    return render(request,'vav/pagina_inicio.html')