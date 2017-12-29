import json
from rest_framework.views import APIView

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer

def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/usuarioRegistrar.html"
	# Si se usa el UserCreationForm en vez de RegistroForm solo se puede indicar los datos de nombre de usuario y contraseña. No se puede indicar Nombre, Apellidos y Correo.
    # form_class = UserCreationForm
	form_class = RegistroForm
	success_url = reverse_lazy('mascota_listar')

class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
