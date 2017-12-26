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

11) 

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