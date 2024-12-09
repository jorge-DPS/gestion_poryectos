from rest_framework import serializers
from .models import Cliente, Proyecto, Empleado, Tarea

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()

    class Meta:
        model = Proyecto
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    proyecto = ProyectoSerializer()
    empleados = EmpleadoSerializer(many=True)

    class Meta:
        model = Tarea
        fields = '__all__'
