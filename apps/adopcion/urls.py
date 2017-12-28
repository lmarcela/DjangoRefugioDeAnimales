from django.urls import path
from django.conf.urls import url, include

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

urlpatterns = [
    path('index/', index_adopcion),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
]