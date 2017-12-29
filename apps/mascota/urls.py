from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, listado

urlpatterns = [
    path('', login_required(index), name='index'),
    path('nuevo/', login_required(mascota_view), name='mascota_crear'),
    path('nuevo2/', login_required(MascotaCreate.as_view()), name='mascota_crear2'),
    path('listar/', login_required(mascota_list), name='mascota_listar'),
    path('listar2', login_required(MascotaList.as_view()), name='mascota_listar2'),
    path('editar/<id_mascota>/', login_required(mascota_edit), name='mascota_editar'),
    path('editar2/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar2'),
    path('eliminar/<id_mascota>/', login_required(mascota_delete), name='mascota_eliminar'),
    path('eliminar2/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar2'),
    path('listado/', login_required(listado), name='listado'),
]
