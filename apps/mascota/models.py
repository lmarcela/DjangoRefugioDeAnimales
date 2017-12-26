from django.db import models

from apps.adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)


class Mascota(models.Model):
    folio = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna)


