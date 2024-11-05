from rest_framework import viewsets

from profesores.models import Profesor
from profesores.serializers import ProfesorSerializer

# Create your views here.
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer