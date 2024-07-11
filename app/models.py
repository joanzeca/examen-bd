from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    fecha_reg = models.DateTimeField(default=timezone.now)
    
    @property
    def promedio(self):
        return (self.nota1 + self.nota2) / 2

    @property
    def condicion(self):
        return "Aprobó" if self.promedio >= 10.5 else "No aprobó"

    def __str__(self):
        return self.nombre
