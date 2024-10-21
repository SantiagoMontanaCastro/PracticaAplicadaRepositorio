from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Video
from .forms import BusquedaForm
from .forms import CalificacionForm
from .models import Compra, Usuario
from .forms import CompraForm

# Create your views here.

#barra de busqueda

def buscar(request):
    form = BusquedaForm()
    resultados = []

    if 'query' in request.GET:
        form = BusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Video.objects.filter(nombre__icontains=query)

    return render(request, 'mi_app/buscar.html', {'form': form, 'resultados': resultados})

#sistema de calificacion

def video_detalle(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    form = CalificacionForm()

    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            estrellas = int(form.cleaned_data['estrellas'])
            video.calificacion = (video.calificacion + estrellas) / 2  
            #promedio de calificaciones
            video.save()
            return redirect('video_detalle', video_id=video.id)

    return render(request, 'mi_app/video_detalle.html', {'video': video, 'form': form})

#sistema de puntos

def realizar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            # se asegura de que el perfil exista
            compra.usuario = request.user.usuario  
            compra.save()
            return redirect('compra_exitosa')
    else:
        form = CompraForm()

    return render(request, 'mi_app/realizar_compra.html', {'form': form})

def compra_exitosa(request):
    return render(request, 'mi_app/compra_exitosa.html')
