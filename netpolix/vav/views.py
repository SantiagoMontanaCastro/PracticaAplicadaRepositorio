from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Carrito 
from .models import AlquilerVenta
from django.contrib import messages  
from .forms import VideoSearchForm 

# Create your views here.



def catalogo_videos(request):
    
    form = VideoSearchForm(request.GET or None)
    # Obtener todos los videos de la base de datos
    videos = Video.objects.all()

    if form.is_valid():
        if form.cleaned_data['ISAN']:
            videos = videos.filter(ISAN=form.cleaned_data['ISAN'])
        if form.cleaned_data['titulo_original']:
            videos = videos.filter(titulo_original__icontains=form.cleaned_data['titulo_original'])
        if form.cleaned_data['ano']:
            videos = videos.filter(ano=form.cleaned_data['ano'])
        if form.cleaned_data['idioma_original']:
            videos = videos.filter(idioma_original__icontains=form.cleaned_data['idioma_original'])
    
    # Renderizar la plantilla y pasar la lista de videos
    return render(request, 'vav/catalogo.html', {'videos': videos})


def alquilar_venta(request, video_id):
    # Obtiene el video correspondiente por su ID
    video = get_object_or_404(Video, id=video_id)

    return render(request, 'vav/alquilar_venta.html', {'video': video})


<<<<<<< HEAD
def pagina_inicio(request):

    return render(request,'vav/pagina_inicio.html')
=======
def agregar_al_carrito(request, video_id, tipo):
    video = get_object_or_404(Video, id=video_id)

    # Verificar si el video ya está en el carrito del usuario con el mismo tipo (alquiler/venta)
    carrito_item = Carrito.objects.filter(usuario=request.user, video=video, tipo=tipo).first()

    if carrito_item:
        # Si el video ya está en el carrito, mostrar un mensaje de advertencia
        messages.warning(request, f"El video '{video.titulo_original}' ya está en tu carrito como {tipo}.")
    else:
        # Si no está, lo agregamos al carrito
        Carrito.objects.create(usuario=request.user, video=video, tipo=tipo)
        messages.success(request, f"El video '{video.titulo_original}' ha sido agregado a tu carrito como {tipo}.")

    return redirect('ver_carrito')  # Redirigir a la página de carrito o donde desees

def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.video.precio_alquiler if item.tipo == 'alquiler' else item.video.precio_venta for item in carrito_items)
    return render(request, 'vav/carrito.html', {'carrito_items': carrito_items, 'total': total})
>>>>>>> 1e3bb5fd193b468f8444de83f1f2f2a8de1e55a0
