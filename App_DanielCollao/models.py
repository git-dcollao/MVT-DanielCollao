from pyexpat import model
from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    