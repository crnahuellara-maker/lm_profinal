from .models import Mensaje

def cantidad_mensajes(request):
    if request.user.is_authenticated:
        cantidad = Mensaje.objects.filter(destinatario=request.user).count()
    else:
        cantidad = 0

    return {
        'cantidad': cantidad
    }
