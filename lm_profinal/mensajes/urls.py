from django.urls import path
from .views import inbox, enviar_mensaje

urlpatterns = [
    path('', inbox, name='inbox'),
    path('enviar/', enviar_mensaje, name='enviar'),
]
