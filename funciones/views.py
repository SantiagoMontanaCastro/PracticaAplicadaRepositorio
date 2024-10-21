from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

#barra de busqueda

def buscar(request):
    query = request.GET.get('q', '')
    resultados = Item.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'mi_app/buscar.html', {'resultados': resultados, 'query': query})


#sistema de calificacion

def agregar_calificacion(request):
    if 1 <= estrellas <= 5:
            self.calificaciones.append(estrellas)
    else:
            None
def promedio_calificacion(self):
    if not self.calificaciones:
            return 0
    return sum(self.calificaciones) / len(self.calificaciones)

def mostrar_calificaciones(self):
    for i, calificacion in enumerate(self.calificaciones, start=1):
        print(f"Calificación: {calificacion} estrella(s)")


#sistema de puntos

def suma_puntos(request, video_id):
    video = Video.objects.get(id=video_id)

    if request.method == 'POST':
        
        transaccion = Transaccion.objects.create(usuario=request.user, video=video, tipo='renta')
        
        request.user.profile.puntos += 1
        request.user.profile.save()

        return redirect('rentar_video', video_id=video.id)

