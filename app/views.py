from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def ingreso(request):
    return HttpResponse("Ingreso")

def listado(request):
    return HttpResponse("Listado")