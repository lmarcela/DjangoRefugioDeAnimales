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



DOCUMENTACION RECOMENDADA:
- https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/
- https://docs.djangoproject.com/en/2.0/topics/db/examples/one_to_one/
- https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/

TIPOS DE RELACIONES EN DJANGO:

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