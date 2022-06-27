from django.db import models

class lista_personas(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
