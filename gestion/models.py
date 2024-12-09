from django.db import models

from django.core.exceptions import ValidationError
from django.utils import timezone

# Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")

    def clean(self):
        if self.fecha_fin < self.fecha_inicio:
            raise ValidationError("La fecha de fin no puede ser antes de la fecha de inicio.")

    def __str__(self):
        return self.nombre

# Empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Tarea
class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")
    empleados = models.ManyToManyField(Empleado, related_name="tareas")

    def clean(self):
        if self.fecha_limite < timezone.now().date():
            raise ValidationError("La fecha límite no puede ser en el pasado.")

    def __str__(self):
        return self.titulo