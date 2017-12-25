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