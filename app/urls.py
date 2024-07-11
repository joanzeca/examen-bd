from django.urls import path
from .views import home, ingreso, listado, api_listado

urlpatterns = [
    path("", home, name="home"),
    path("ingreso/", ingreso, name="ingreso"),
    path("listado/", listado, name="listado"),
    path("api/listado/", api_listado, name="api_listado"),
]