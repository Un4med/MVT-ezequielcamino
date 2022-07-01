from django.urls import path
from .views import una_vista, listado

urlpatterns = [
    path('', una_vista),
    path('listado/', listado),
]