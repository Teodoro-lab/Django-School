from rest_framework import viewsets

from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializer

# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer