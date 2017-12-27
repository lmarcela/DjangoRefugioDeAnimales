from django.urls import path
from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
]
