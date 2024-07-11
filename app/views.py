from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def ingreso(request):
    return render(request, "ingreso.html")

def listado(request):
    return render(request, "listado.html")