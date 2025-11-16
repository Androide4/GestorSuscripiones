from django.contrib import admin
from .models import (
    Proveedor, Moneda, Plan, MetodoPago, Suscripcion,
    Pago, Notificacion, Comentario
)
# Register your models here.
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'sitio_web', 'creado_en')
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ('nombre', 'categoria')


@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'simbolo', 'decimales', 'ultima_actualizacion')
    search_fields = ('codigo',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proveedor', 'duracion_dias', 'precio', 'moneda', 'creado_en')
    search_fields = ('nombre', 'proveedor__nombre')
    list_filter = ('proveedor', 'moneda')


@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('get_tipo_display', 'ultimos4', 'marca', 'es_predeterminado', 'creado_en')
    list_filter = ('tipo', 'es_predeterminado')
    search_fields = ('token', 'ultimos4')

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
    get_tipo_display.short_description = "Tipo"


@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'plan', 'estado', 'fecha_inicio', 'fecha_fin', 'moneda', 'renovacion_automatica')
    list_filter = ('estado', 'moneda', 'proveedor', 'renovacion_automatica')
    search_fields = ('proveedor__nombre', 'plan__nombre', 'descripcion')
    date_hierarchy = 'fecha_inicio'


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'monto', 'moneda', 'estado', 'referencia', 'pagado_en', 'creado_en')
    list_filter = ('estado', 'moneda')
    search_fields = ('referencia', 'suscripcion__proveedor__nombre')


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'get_tipo_display', 'enviar_en', 'enviado_en', 'leida')
    list_filter = ('tipo', 'leida', 'enviar_en')
    search_fields = ('suscripcion__proveedor__nombre',)

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
    get_tipo_display.short_description = "Tipo"


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'texto_corto', 'creado_en')
    search_fields = ('texto', 'suscripcion__proveedor__nombre')
    ordering = ('-creado_en',)

    def texto_corto(self, obj):
        return (obj.texto[:50] + '...') if len(obj.texto) > 50 else obj.texto
    texto_corto.short_description = "Comentario"