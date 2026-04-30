from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

    path('pages/', PageList.as_view(), name='pages'),

    path('pages/<int:pk>/', PageDetail.as_view(), name='detalle'),

    path('pages/crear/', PageCreate.as_view(), name='crear'),
    path('pages/<int:pk>/editar/', PageUpdate.as_view(), name='editar'),
    path('pages/<int:pk>/borrar/', PageDelete.as_view(), name='borrar'),
]
