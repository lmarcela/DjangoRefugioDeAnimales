from django.urls import path
from django.conf.urls import url, include

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('index/', index_adopcion),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<pk>/', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]