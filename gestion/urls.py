from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProyectoViewSet, EmpleadoViewSet, ProyectosActivos, TareaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/proyectos/activos/', ProyectosActivos.as_view(), name='proyectos-activos'),  # Ruta para la API personalizada
]
