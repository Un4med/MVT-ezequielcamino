from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
from .models import Listado


# Create your views here.

def una_vista(request):
    return HttpResponse('<h1> la pipol</h1>')

#en las variables pruebas, me pidió los ID de los objetos a guardar en la DB, es por eso que los puse. 
def listado(request):
    
    cargando = loader.get_template('listado.html')

    prueba1 = Listado(1,'pepito', 78)
    prueba2 = Listado(2,'juancito',56)
    prueba3 = Listado(3,'manuelita',15)
    prueba1.save()
    prueba2.save()
    prueba3.save()
    render = cargando.render({'listado':[prueba1, prueba2, prueba3]})

    return HttpResponse(render)