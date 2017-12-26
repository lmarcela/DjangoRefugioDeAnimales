1) Seguir los pasos (1-10) para creacion de ambiente (test19) y activacion del mismo disponibles en README.md de https://github.com/lmarcela/DjangoFirstApp
2) Empezar un proyecto en el ambiente:
	E:\PYTHON\DJANGO\ambientes\test19\Scripts>activate
	(test19) E:\PYTHON\DJANGO\ambientes\test19\Scripts>cd ..

	(test19) E:\PYTHON\DJANGO\ambientes\test19>cd ..

	(test19) E:\PYTHON\DJANGO\ambientes>cd ..

	(test19) E:\PYTHON\DJANGO>cd proyectos

	(test19) E:\PYTHON\DJANGO\proyectos>django-admin.py startproject RefugioDeAnimales

3) Explicacion de la configuracion del proyecto
	El archivo manage.py es el empaquetador del djangoadmin
	El archivo _init_ es el que indica que es un paquete de python
	Otros archivos son settings, urls y wsgi.

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


GIT COMMANDS:
…or create a new repository on the command line

echo "# DjangoRefugioDeAnimales" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/lmarcela/DjangoRefugioDeAnimales.git
git push -u origin master
…or push an existing repository from the command line

git remote add origin https://github.com/lmarcela/DjangoRefugioDeAnimales.git
git push -u origin master