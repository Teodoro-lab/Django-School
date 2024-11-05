from django.db import models

# Create your models here.
class Profesor(models.Model):
    numeroEmpleado = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    horasClase = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"