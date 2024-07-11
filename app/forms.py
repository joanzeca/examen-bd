# En forms.py
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'curso', 'nota1', 'nota2']  # Campos que quieres incluir en el formulario
