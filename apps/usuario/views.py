from django.shortcuts import render
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/usuarioRegistrar.html"
	# Si se usa el UserCreationForm en vez de RegistroForm solo se puede indicar los datos de nombre de usuario y contraseña. No se puede indicar Nombre, Apellidos y Correo.
    # form_class = UserCreationForm
	form_class = RegistroForm
	success_url = reverse_lazy('mascota_listar')


