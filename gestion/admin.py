from django.contrib import admin

from .models import Cliente, Proyecto, Empleado, Tarea

admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Empleado)
admin.site.register(Tarea)