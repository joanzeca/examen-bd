from django.shortcuts import render
from django.http import Http404
from .models import Alumno

# Create your views here.

def home(request):
    return render(request, "home.html")

def ingreso(request):
    return render(request, "ingreso.html")

def listado(request):
    try:
        alumnos = Alumno.objects.all()
    except ValueError:
        raise Http404("Alumnos no encontrados.", ValueError)
    
    return render(request, "listado.html", {"alumnos":alumnos})