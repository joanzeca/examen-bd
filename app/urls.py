from django.urls import path
from .views import home, ingreso, listado 

urlpatterns = [
    path("", home),
    path("ingreso/", ingreso),
    path("listado/", listado),
]