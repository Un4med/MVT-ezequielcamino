from django.urls import path
from .views import una_vista, Listado

urlpatterns = [
    path('', una_vista),
    path('listado/', Listado),
]