from django.urls import path
from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('listar/', mascota_list, name='mascota_listar'),
    path('editar/<id_mascota>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<id_mascota>/', mascota_delete, name='mascota_eliminar'),
]
