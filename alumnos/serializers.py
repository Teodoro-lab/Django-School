from rest_framework import serializers
from alumnos.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'nombres', 'apellidos', 'matricula', 'promedio']