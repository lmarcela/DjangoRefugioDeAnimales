from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.usuario.views import RegistroUsuario, listadousuarios

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    path('listado/', login_required(listadousuarios), name='usuario_listado'),
]
