from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from .models import Alumno
from django.core.serializers import serialize
from .forms import AlumnoForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def ingreso(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto Alumno en la base de datos
            return redirect('ingreso')  # Redirige a alguna página de éxito o a la lista de alumnos
    else:
        form = AlumnoForm()
    
    return render(request, "ingreso.html", {'form': form})

def listado(request):
    try:
        alumnos = Alumno.objects.all()
    except ValueError:
        raise Http404("Ha ocurrido un error al hacer la consulta a la tabla Alumno.", ValueError)
    
    return render(request, "listado.html", {"alumnos":alumnos})

def api_listado(request):
    try:
        alumnos = Alumno.objects.all().values()
        alumnos_list = list(alumnos)
        # Agregar la propiedad 'condicion' a cada alumno
        for alumno in alumnos_list:
            alumno_obj = Alumno.objects.get(id=alumno['id'])  # Suponiendo que 'id' es la clave primaria
            alumno['condicion'] = alumno_obj.condicion
            alumno['promedio'] = alumno_obj.promedio
            alumno['fecha_reg'] = alumno_obj.fecha_reg.strftime("%d-%m-%Y")
    except ValueError:
        raise Http404("Ha ocurrido un error al hacer la consulta a la tabla Alumno.", ValueError)
    
    return JsonResponse(alumnos_list, safe=False)