from django.urls import path
from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('nuevo2/', MascotaCreate.as_view(), name='mascota_crear2'),
    path('listar/', mascota_list, name='mascota_listar'),
    path('listar2/', MascotaList.as_view(), name='mascota_listar2'),
    path('editar/<id_mascota>/', mascota_edit, name='mascota_editar'),
    path('editar2/<pk>/', MascotaUpdate.as_view(), name='mascota_editar2'),
    path('eliminar/<id_mascota>/', mascota_delete, name='mascota_eliminar'),
    path('eliminar2/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar2'),
]
