from django.db import models

#Create models here
class Listado(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'me llamo {self.nombre}'