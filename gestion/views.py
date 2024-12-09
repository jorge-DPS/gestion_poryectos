from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Proyecto, Empleado, Tarea
from .serializers import ClienteSerializer, ProyectoSerializer, EmpleadoSerializer, TareaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Proyecto
from .serializers import ProyectoSerializer
from datetime import date

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class ProyectosActivos(APIView):
    def get(self, request):
        proyectos = Proyecto.objects.filter(fecha_fin__gte=date.today())
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
