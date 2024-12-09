from django.forms import ValidationError
from rest_framework import serializers
from .models import Cliente, Proyecto, Empleado, Tarea

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# class ProyectoSerializer(serializers.ModelSerializer):
#     cliente = ClienteSerializer()

#     class Meta:
#         model = Proyecto
#         fields = '__all__'

#     def validate(self, data):
#         # Llamar al método full_clean() del modelo para validar las validaciones personalizadas
#         proyecto = Proyecto(**data)
#         try:
#             proyecto.full_clean()  # Esto aplica las validaciones del modelo
#         except ValidationError as e:
#             raise serializers.ValidationError(e.message_dict)  # Pasa los errores de validación a DRF

#         return data  # Si no hay errores, retorna los datos validados

class ProyectoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta:
        model = Proyecto
        fields = '__all__'

    def validate(self, data):
        # Llamar al método full_clean() del modelo para validar las validaciones personalizadas
        proyecto = Proyecto(**data)
        try:
            proyecto.full_clean()  # Esto aplica las validaciones del modelo
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)  # Pasa los errores de validación a DRF

        return data  # Si no hay errores, retorna los datos validados

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    empleados = serializers.PrimaryKeyRelatedField(queryset=Empleado.objects.all(), many=True)
    proyecto = serializers.PrimaryKeyRelatedField(queryset=Proyecto.objects.all())

    # proyecto = ProyectoSerializer()
    # empleados = EmpleadoSerializer(many=True)

    class Meta:
        model = Tarea
        fields = '__all__'

    # def validate(self, data):
    #     """
    #     Realiza la validación personalizada del modelo Tarea
    #     """
    #     tarea = Tarea(**data)
    #     try:
    #         tarea.full_clean()  # Ejecuta las validaciones personalizadas (como la de fecha_limite)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e.message_dict)  # Propaga los errores a DRF

    #     # Validar y asignar la relación many-to-many correctamente
    #     if 'empleados' in data:
    #         empleados = data['empleados']  # Lista de empleados recibida en los datos
    #         tarea.empleados.set(empleados)  # Asigna los empleados a la relación many-to-many usando .set()

    #     return data  # Retorna los datos validados
