from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"