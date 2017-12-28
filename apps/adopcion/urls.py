from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('index/', login_required(index_adopcion)),
    path('solicitud/listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    path('solicitud/editar/<pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    path('solicitud/eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]