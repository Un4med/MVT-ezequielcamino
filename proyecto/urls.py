from django.urls import path
from .views import una_vista, lista_personas

urlpatterns = [
    path('', una_vista),
    path('listado/', lista_personas),
]