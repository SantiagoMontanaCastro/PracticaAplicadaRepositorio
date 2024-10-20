class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar(self, video):
        video_id = str(video.id)
        if video_id not in self.carrito:
            self.carrito[video_id] = {
                'titulo': video.titulo_original,
                'precio': 10.0,  # Puedes ajustar el precio dependiendo de si es compra o alquiler
                'cantidad': 1,
            }
        else:
            self.carrito[video_id]['cantidad'] += 1
        self.guardar()

    def guardar(self):
        self.session.modified = True

    def eliminar(self, video):
        video_id = str(video.id)
        if video_id in self.carrito:
            del self.carrito[video_id]
            self.guardar()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True
