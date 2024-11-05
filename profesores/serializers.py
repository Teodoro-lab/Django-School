from rest_framework import serializers
from profesores.models import Profesor

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['id', 'numeroEmpleado', 'nombres', 'apellidos', 'horasClase']