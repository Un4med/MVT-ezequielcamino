from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
from proyecto.models import lista_personas

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1> la pipol</h1>')


def listado(request):
    
    template = loader.get_template('listado.html')


    template1 = lista_personas.objects.all()

    render = template.render({'lista_personas': template1})

    return HttpResponse(render)