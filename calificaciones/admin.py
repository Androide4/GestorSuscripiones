from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'puntuacion',)
    search_fields = ('suscripcion__proveedor__nombre',)