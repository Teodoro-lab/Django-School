from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alumnos.views import AlumnoViewSet
from profesores.views import ProfesorViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)
router.register(r'profesores', ProfesorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),  # Include the router's endpoints
]
