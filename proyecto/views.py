from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
from .models import Listado


# Create your views here.

def una_vista(request):
    return HttpResponse('<h1> la pipol</h1>')


def listado(request):
    
    template = loader.get_template('listado.html')

    prueba1 = Listado('pepe', 34)
    prueba2 = Listado('juancito', 4)
    prueba3 = Listado('jacinto', 56)
    prueba1.save()
    prueba2.save()
    prueba3.save()
    render = Template.render({'listado':[prueba1,prueba2,prueba3]})

    return HttpResponse(render)