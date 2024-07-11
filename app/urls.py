from django.urls import path
from .views import home, ingreso, listado 

urlpatterns = [
    path("", home, name="home"),
    path("ingreso/", ingreso, name="ingreso"),
    path("listado/", listado, name="listado"),
]