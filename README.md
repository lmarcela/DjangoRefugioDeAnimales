# PASOS

1) Seguir los pasos (1-10) para creacion de ambiente (test19) y activacion del mismo disponibles en README.md de https://github.com/lmarcela/DjangoFirstApp
2) Empezar un proyecto en el ambiente:

		E:\PYTHON\DJANGO\ambientes\test19\Scripts>activate
		(test19) E:\PYTHON\DJANGO\ambientes\test19\Scripts>cd ..

		(test19) E:\PYTHON\DJANGO\ambientes\test19>cd ..

		(test19) E:\PYTHON\DJANGO\ambientes>cd ..

		(test19) E:\PYTHON\DJANGO>cd proyectos

		(test19) E:\PYTHON\DJANGO\proyectos>django-admin.py startproject RefugioDeAnimales

3) Explicacion de la configuracion del proyecto

	- El archivo manage.py es el empaquetador del djangoadmin
	- El archivo _init_ es el que indica que es un paquete de python
	- Otros archivos son settings, urls y wsgi.

4) Con el fin de organizar las aplicaciones se crea una carpeta llamada apps que contenga todas las aplicaciones. Para que la carpeta sea reconocida como un paquete de python dentro se crea el archivo init (_init_.py).

5) Dentro de apps crear la app para mascota:

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales\apps>django-admin.py startapp mascota

6) Dentro de apps crear la app para adopcion:

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales\apps>django-admin.py startapp adopcion

7) Para que las app sean reconocidas hay que modificar la variable INSTALLED_APPS de settings.py

		INSTALLED_APPS = [
			...
			'apps.adopcion',
			'apps.mascota',
		]

8) Para configurar la bd en settings.py:

		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql',
				'NAME': 'refugioDjango',
				'USER': 'root', 
				'PASSWORD': 'root', 
				'HOST': 'localhost',
				'PORT': 3307,
			}
		}

9) Para configurar el lenguaje en settings.py:
	
		LANGUAGE_CODE = 'es-co'

10) Para migrar la bd se crea una bd vacia de nombre refugioDjango en mysql y luego se ejecuta el comando manage.py migrate:
	
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py migrate

11) Los modelos se escriben en el archivo models.py de la app correspondiente. Para el modelo de mascota:
	
			from django.db import models

			# Create your models here.

			class Mascota(models.Model):
				nombre = models.CharField(max_length=50)
				sexo = models.CharField(max_length=10)
				edad_aproximada = models.IntegerField()
				fecha_rescate = models.DateField()
		
	Para el modelo de adopcion:
	
			from django.db import models

			# Create your models here.

			class Persona(models.Model):
				nombre = models.CharField(max_length=50)
				apellidos = models.CharField(max_length=70)
				edad = models.IntegerField()
				telefono = models.CharField(max_length=12)
				email = models.EmailField()
				domicilio = models.TextField()

	Para saber mas sobre los tipos de dato ver: https://docs.djangoproject.com/en/2.0/ref/models/fields/

	Por defecto python crea un id autoincremental para cada modelo pero si quisiera definir uno propio, entonces:
    
		folio = models.CharField(max_length=10,primary_key=True)

12) Para hacer las migraciones de los modelos configurados se ejecuta el comando manage.py makemigrations en la raiz del proyecto:
	
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py makemigrations

13) Para pasar la migracion a la bd se ejecuta el comando manage.py migrate
	
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py migrate

14) En mysql crea 2 tablas con la sintaxis nombreApp_modelo:
	- adopcion_persona
	- mascota_mascota

15) Crear relacion de 1 (Persona) a N (Mascota). Luego hacer migracion:

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py makemigrations

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py migrate

16) Para poder manipular los modelos desde el administrador de django:
	- se configura el archivo admin.py de cada app de la forma admin.site.register(NombreDelModelo)
	- Crear un superusuario: manage.py createsuperuser 
		
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py createsuperuser 
			NOTA user: marcela; password: abcdmarcela.
	- Correr el servidor: manage.py runserver (test19) 

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py runserver

	- Acceso a http://localhost:8000/admin con los datos del usuario creado. Probar el registro de una persona, una mascota, una vacuna desde el administrador de django. Si por ejemplo se elimina una mascota automaticamente se borra la relacion que tenia con vacuna.

17) Modificacion en el modelo Mascota:
	- Se borro la llave primaria para que funcione con la de defecto. 
	- Se añade el parametro blank en la relacion a Vacuna
		
		class Mascota(models.Model):
			nombre = models.CharField(max_length=50)
			sexo = models.CharField(max_length=10)
			edad_aproximada = models.IntegerField()
			fecha_rescate = models.DateField()
			persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
			vacuna = models.ManyToManyField(Vacuna,blank=True)
	
	Para que las migraciones no generen conflicto la manera mas facil es borrar todas las tablas de la base de datos.
	Borrar todos los archivos 0xxx_initial.py ubicado en \apps\mascota\migrations\.
	Luego se ejecutan los comandos de migracion:

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py makemigrations
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py migrate

18) Volver a Crear un superusuario: manage.py createsuperuser 
		
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py createsuperuser 
			NOTA user: marcela; password: abcdmarcela.

19) Importar los modelos. Abrir el shell de django: manage.py shell

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py shell

- En el shell:

>>from apps.mascota.models import Vacuna, Mascota

>>from apps.adopcion.models import Persona

/*La primer forma de crear un objeto*/

>>Persona.objects.create(nombre="Lina", apellidos="Gomez", edad=34, telefono="867", email="lina@mail.com", domicilio = "cra 867")

>>p = Persona(nombre="Marcela", apellidos="Malaver", edad=22, telefono="878", email="marce@mail.com", domicilio = "cra 69")
>>p.save()


>>m = Mascota(nombre="Kiara", sexo="macho", edad_aproximada=2, fecha_rescate="2017-01-09", persona=p)

>>m.save()

>>v1 = Vacuna(nombre="vacuna 1")

>>v1.save()

>>v2 = Vacuna(nombre="vacuna 2")

>>v2.save()

/*Agregar la llave foranea*/

>>m.vacuna.add(v1,v2)

/*Ya no es necesario llamar al metodo save*/


/*Consultas*/

>>Persona.objects.all()

Respuesta: <QuerySet [<Persona: Persona object (1)>, <Persona: Persona object (2)>]>

>>Persona.objects.filter(id=2)

Respuesta: <QuerySet [<Persona: Persona object (2)>]>

>>Persona.objects.filter(nombre__contains="Lina")

Respuesta: <QuerySet [<Persona: Persona object (1)>]>

20) Configurar url y views de las apps. 
- Modificar archivo views.py de cada app. Por ahora cada una solamente imprime un texto.
- Crear archivo urls.py para cada app. Aqui se define la configuracion local.
- Modificar archivo urls.py del proyecto. Aqui se define la configuracion global.
Nuevas url de acceso:
http://localhost:8000/mascota/, http://localhost:8000/adopcion/index/

21) Definir el template en la variable TEMPLATES de settings.py:

		TEMPLATES = [
			{
				...
				'DIRS': [os.path.join(BASE_DIR,'templates')],
				'APP_DIRS': True,
				...
			},
		]

	Se recomienda ver la seccion SISTEMA DE PLANTILLAS DE DJANGO.

22) Herencia de templates de django.
- Crear carpeta "templates" en la base del proyecto. Dentro crear la carpeta "base". Dentro de "base" crear el archivo "base.html". En este archivo se definen bloques que pueden modificarse dentro de otros html. Para demostracion de los include se realizo un include de "header.html" en "base.html".
- Para los templates de la app mascota se creo una carpeta llamada "mascota" dentro de la carpeta "templates". Dentro se hizo la prueba de sobreescribir ciertos bloques.
- Se modifico el archivo views.py de mascota para poder mostrar el html de "index.html". (render(request,'mascota/index.html'))

23) Configurar archivos estaticos del proyecto:
- carpeta "static" contiene js y css.
- Referencia a carpeta static en settings.py: 
	
		STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
- Nuevo html para uso de plantilla bootstrap https://bootswatch.com/flatly/ en base.html e index.html (de mascota). css y js de la carpeta static añadidos en base.html.

24) Formulario de crear mascota:
- configuracion de apps/mascota/urls.py: 
	
		path('nuevo/', mascota_view, name='mascota_crear'),

- configuracion de apps/mascota/views.py: 

		def mascota_view(request):
		if request.method=='POST':
			form = MascotaForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('index')
		else:
			form = MascotaForm()
		return render(request,'mascota/mascotaForm.html',{'form':form})

- configuracion de apps/mascota/forms.py: fields, labels, widgets.
- configuracion de templates/mascota/mascotaForm.html: 

		{% extends 'base/base.html' %} 

		{% block content %}
		<br>
		<form method="post">
				{% csrf_token %}
				{{ form.as_p }}

				<button type="submit">Guardar</button>
		</form>
		{% endblock %}

- Modificar el modelo de Persona (apps/adopcion/models.py) para visualizar el nombre y apellido en vez del objeto:

		def __str__(self):
			return '{}'.format(self.nombre+" "+self.apellidos)

- Modificar el modelo de Vacuna (apps/mascota/models.py) para visualizar el nombre en vez del objeto:
	
		def __str__(self):
			return '{}'.format(self.nombre)

25) Listar registros de Mascota (vista basada en funciones):
- configuracion de templates/mascota/mascotaList.html: uso de variables, bloques if, else, for.
- configuracion de apps/mascota/views.py: 

		def mascota_list(request):
			mascota = Mascota.objects.all()
			contexto = {'mascotas':mascota}
			return render(request,'mascota/mascotaList.html',contexto)

- configuracion de apps/mascota/urls.py: 

    	path('listar/', mascota_list, name='mascota_listar'),

26) Actualizar y eliminar registros de Mascota (vista basada en funciones):
- configuracion de templates/mascota/mascotaDelete.html: uso de variables.
- configuracion de templates/mascota/mascotaList.html: Adicion de acciones editar y eliminar.
- configuracion de apps/mascota/views.py: 

		def mascota_edit(request,id_mascota):
			mascota = Mascota.objects.get(id=id_mascota)
			if request.method=='GET':
				form = MascotaForm(instance=mascota)
			else:
				form = MascotaForm(request.POST,instance=mascota)
				if form.is_valid():
					form.save()
				return redirect('mascota_listar')
			return render(request,'mascota/mascotaForm.html',{'form':form})

		def mascota_delete(request,id_mascota):
			mascota = Mascota.objects.get(id=id_mascota)
			if request.method=='POST':
				mascota.delete()
				return redirect('mascota_listar')
			return render(request,'mascota/mascotaDelete.html',{'mascota':mascota})

- configuracion de apps/mascota/urls.py: 

		path('editar/<id_mascota>/', mascota_edit, name='mascota_editar'),
		path('eliminar/<id_mascota>/', mascota_delete, name='mascota_eliminar'),

27) App Mascota. Vistas basadas en clases (ListView & CreateView):
- configuracion de templates/mascota/mascotaList2.html: Modificacion con respecto a mascotaList.html por la obtencion de datos a traves de la clase.
- configuracion de apps/mascota/views.py: ListView & CreateView

	class MascotaList(ListView):
		model = Mascota
		template_name = 'mascota/mascotaList2.html'

	class MascotaCreate(CreateView):
		model = Mascota
		form_class = MascotaForm
		template_name = 'mascota/mascotaForm.html'
		success_url = reverse_lazy('mascota_listar2')

- configuracion de apps/mascota/urls.py: 
		
    	path('nuevo2/', MascotaCreate.as_view(), name='mascota_crear2'),
    	path('listar2/', MascotaList.as_view(), name='mascota_listar2'),

28) App Mascota. Vistas basadas en clases (UpdateView & DeleteView):
- configuracion de templates/mascota/mascotaList2.html: Modificacion con respecto a mascotaList.html por la obtencion de datos a traves de la clase.
- configuracion de templates/mascota/mascotaDelete2.html: Modificacion con respecto a mascotaDelete.html por la obtencion de datos a traves de la clase.
- configuracion de apps/mascota/views.py: UpdateView & DeleteVie

		class MascotaUpdate(UpdateView):
			model = Mascota
			form_class = MascotaForm
			template_name = 'mascota/mascotaForm.html'
			success_url = reverse_lazy('mascota_listar2')

		class MascotaDelete(DeleteView):
			model = Mascota
			template_name = 'mascota/mascotaDelete2.html'
			success_url = reverse_lazy('mascota_listar2')

- configuracion de apps/mascota/urls.py: 
		    	
    	path('editar2/<pk>/', MascotaUpdate.as_view(), name='mascota_editar2'),,
    	path('eliminar2/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar2'),

29) CRUD con dos formularios. Primera parte (List & Create):
- Class Solicitud en apps/adopcion/models.py:

		class Solicitud(models.Model):
			persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)
			numero_mascotas = models.IntegerField()
			razones = models.TextField()

- manage.py makemigrations

		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py makemigrations
- manage.py migrate
		
		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales>manage.py migrate
- Configuracion de apps/adopcion/forms.py: Formulario para Persona y Solicitud
- Configuracion de apps/adopcion/urls.py:

		path('index/', index_adopcion),
		path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
		path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),

Accesos a:

			http://localhost:8000/adopcion/solicitud/listar
			http://localhost:8000/adopcion/solicitud/nueva
			
- Configuracion de apps/adopcion/views.py: SolicitudList & SolicitudCreate
- Configuracion de templates/adopcion: solicitudForm.html & solicitudList.html

30) CRUD con dos formularios. Segunda parte (Update & Delete):
- Configuracion de apps/adopcion/urls.py:

		path('solicitud/editar/<pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
		path('solicitud/eliminar/<pk>/', SolicitudDelete.as_view(), name='solicitud_eliminar'),

Accesos a:

			http://localhost:8000/adopcion/solicitud/editar/1 ("idSolicitud")
			http://localhost:8000/adopcion/solicitud/eliminar/1 ("idSolicitud")
			
- Configuracion de apps/adopcion/views.py: SolicitudUpdate & SolicitudDelete
- Configuracion de templates/adopcion: solicitudDelete.html

31) Nueva app Usuarios. Crear Registro de usuarios.
- Dentro de apps crear la app para usuario:django-admin.py startapp usuario

 		(test19) E:\PYTHON\DJANGO\proyectos\RefugioDeAnimales\apps>django-admin.py startapp usuario

- Añadir la app en RefugioDeAnimales/settings.py :
		
		INSTALLED_APPS = [
			...
			'apps.usuario',
		]
- Configuracion de apps/usuario/urls.py:
	
    	path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),


- Configuracion de apps/usuario/forms.py: fields and labels

- Configuracion de apps/usuario/views.py: RegistroUsuario(CreateView).

- Configuracion de RefugioDeAnimales/urls.py:

    	path('usuario/', include('apps.usuario.urls'),name="usuario"),

- Configuracion de templates/usuario/usuarioRegistrar.html

32) Crear Login:
- Configuracion de RefugioDeAnimales/urls.py. No olvidar from django.contrib.auth.views import login

	    path('',login,kwargs={'template_name': 'index.html'}, name="login"),

- Configuracion de RefugioDeAnimales/settings.py: La variable LOGIN_REDIRECT_URL le indica a la app a que pagina redirigirse tan pronto el login es exitoso. No olvidar from django.urls import reverse_lazy

		LOGIN_REDIRECT_URL = reverse_lazy('solicitud_listar')
- Configuracion de templates/index.html. Formulario de inicio de sesión.

33) Restriccion de urls para usuarios no logueados. Adicion de funcionalidades al menú:
- Modificacion en RefugioDeAnimales/urls.py. No olvidar 
from django.contrib.auth.views import login, logout_then_login

		path('accounts/login/',login,kwargs={'template_name': 'index.html'}, name="login"),
		path('logout/',logout_then_login, name="logout"),
- Modificacion en apps/adopcion/urls.py: No olvidar from django.contrib.auth.decorators import login_required

		urlpatterns = [
			path('index/', login_required(index_adopcion)),
			path('solicitud/listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
			path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
			path('solicitud/editar/<pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
			path('solicitud/eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
		]

- Modificacion en apps/mascota/urls.py: No olvidar from django.contrib.auth.decorators import login_required

		urlpatterns = [
			path('', login_required(index), name='index'),
			path('nuevo/', login_required(mascota_view), name='mascota_crear'),
			path('nuevo2/', login_required(MascotaCreate.as_view()), name='mascota_crear2'),
			path('listar/', login_required(mascota_list), name='mascota_listar'),
			path('listar2/', login_required(MascotaList.as_view()), name='mascota_listar2'),
			path('editar/<id_mascota>/', login_required(mascota_edit), name='mascota_editar'),
			path('editar2/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar2'),
			path('eliminar/<id_mascota>/', login_required(mascota_delete), name='mascota_eliminar'),
			path('eliminar2/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar2'),
		]

- Modificacion en templates/base/base.html. Adicion de urls a los menus:

		<a class="dropdown-item" href="{% url 'mascota_crear' %}">Registrar</a>
		<a class="dropdown-item" href="{% url 'mascota_crear' %}">Registrar</a>
		<a class="dropdown-item" href="{% url 'mascota_listar2' %}">Listar</a>
		<a class="dropdown-item" href="{% url 'solicitud_crear' %}">Solicitar</a>
		<a class="dropdown-item" href="{% url 'solicitud_listar' %}">Listar solicitudes</a>
		<a class="dropdown-item" href="{% url 'logout' %}">Salir</a>

34) Recuperar contraseña por correo.
- En el correo de gmail activar el acceso de aplicaciones menos seguras en: https://myaccount.google.com/security (Permitir el acceso de aplicaciones menos seguras: SÍ.)

- RefugioDeAnimales/settings.py: Añadir configuracion para email que servira para el envio de recuperacion de contraseñas. Modificar user y password.

		EMAIL_USE_TLS = True
		EMAIL_HOST = 'smtp.gmail.com'
		EMAIL_PORT = 25
		EMAIL_HOST_USER = 'pruebasmarcelamalaver@gmail.com'
		EMAIL_HOST_PASSWORD = '*******'
		EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

- RefugioDeAnimales/urls.py: Añadir path para recuperacion de contraseña. No olvidar: from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_confirm, password_reset_done, password_reset_complete.

		#passwordResetPaths
		path('reset/passwordReset', password_reset, kwargs={'template_name':'passwordReset/passwordResetForm.html','email_template_name': 'passwordReset/passwordResetEmail.html'}, name='password_reset'), 

		path('reset/passwordResetDone', password_reset_done, kwargs={'template_name': 'passwordReset/passwordResetDone.html'}, name='password_reset_done'),

		path('reset/<uidb64>[0-9A-Za-z_\-]/<token>', password_reset_confirm, kwargs={'template_name': 'passwordReset/passwordResetConfirm.html'}, name='password_reset_confirm'),

		path('reset/done', password_reset_complete, kwargs={'template_name': 'passwordReset/passwordResetComplete.html'}, name='password_reset_complete'),

- templates/index.html: Añadir url para recuperacion de contraseña. 

		<a href="{% url 'password_reset' %}">Olvidé mi contraseña</a>

- Añadir templates para recuperacion de contraseña. 

		templates/passwordReset/passwordResetComplete.html
		templates/passwordReset/passwordResetConfirm.html
		templates/passwordReset/passwordResetDone.html
		templates/passwordReset/passwordResetEmail.html
		templates/passwordReset/passwordResetForm.html

35) Serializar objetos de los modelos para posteriormente poder utilizarlos como servicio web:
- apps/mascota/views.py: No olvidar from django.core import serializers:

		def listado(request):
			lista = serializers.serialize('json', Mascota.objects.all())
			return HttpResponse(lista, content_type='application/json')
- apps/mascota/urls.py:	
		
    	path('listado/', login_required(listado), name='listado'),

- apps/usuario/urls.py:

    	path('listado/', login_required(listadousuarios), name='usuario_listado'),
- apps/usuario/views.py:

		def listadousuarios(request):
			lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
			return HttpResponse(lista, content_type='application/json')

36) Paginación en listar mascota.

- apps/mascota/urls.py. Cambiar url para listar mascota:
    	
		path('listar2', login_required(MascotaList.as_view()), name='mascota_listar2'),

- apps/mascota/views.py. Indicar cuantos registros mostrar por pagina en MascotaList. En este caso se indicaron 5:

		class MascotaList(ListView):
			model = Mascota
			template_name = 'mascota/mascotaList2.html'
			paginate_by = 5

- templates/mascota/mascotaList2.html: Se configuraron 3 estilos de paginacion. El primero funciona con los botones previous y next. El segundo muestra first, previous, el numero de pagina actual, next y last. El tercero muestra first, numeros de pagina y last.


# TIPOS DE RELACIONES EN DJANGO:

## Documentacion recomendada:
- https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/
- https://docs.djangoproject.com/en/2.0/topics/db/examples/one_to_one/
- https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/

## Tipos
- 1 A N: (1 persona puede adoptar mas de una mascota)
	class Persona(models.Model):
		atributos...
	
	class Mascota(models.Model):
		persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
		atributos...

- 1 A 1: (caso en que una persona solo pueda adoptar una mascota)
	class Persona(models.Model):
		atributos...
	
	class Mascota(models.Model):
		persona = models.OneToOneField(Persona,null=True,blank=True,on_delete=models.CASCADE)
		atributos...

- N A N: (1 mascota puede tener aplicadas varias vacunas y 1 vacuna puede estar aplicada a varias mascotas):
	class Vacuna(models.Model):
		atributos...
	
	class Mascota(models.Model):
		vacuna = models.ManyToManyField(Vacuna)
		atributos...

# SISTEMA DE PLANTILLAS DE DJANGO

El sistema de plantillas de django permite separar la logica de la aplicacion de la parte visual (html). Provee 3 herramientas:
- Variables: Encerradas entre llaves dobles ({{}}). El contexto es la informacion enviada por la vista al template en forma de un diccionario.
- Tags (etiquetas): Se encuentran cerrados entre llaves y signos de porcentaje ({% for xxx in yyy %}). Permite: hacer flujos de control (bucle for, sentencia if) de informacion externa del template, cargar archivos estaticos en el template ( {% load staticfiles %} ).
- Herencia de plantillas: Reduce la duplicacion y redundancia de elementos comunes de los templates como title, header, navbar, footer. Lo que se hace es crear un archivo base que va a contener a todos y en otros templates poder heredarlos con extends. Estos se definen en la variable TEMPLATES de settings.py. Se modifica el DIRS.

# GIT COMMANDS:
		git init
		git add .
		git commit -m "first commit"
		git remote add origin https://github.com/lmarcela/DjangoRefugioDeAnimales.git
		git push -u origin master
