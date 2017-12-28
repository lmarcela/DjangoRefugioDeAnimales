from django.urls import path
from django.conf.urls import url, include

from apps.usuario.views import RegistroUsuario

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
]
