from django import forms
from .models import Suscripcion, Proveedor, Moneda, Plan, MetodoPago, Comentario

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = '__all__'
        labels = {
            'proveedor': 'Proveedor *',
            'plan': 'Plan',
            'fecha_inicio': 'Fecha de Inicio *',
            'fecha_fin': 'Fecha de Fin *',
            'renovacion_automatica': 'Renovación Automática',
            'estado': 'Estado *',
            'moneda': 'Moneda *',
            'descripcion': 'Descripción (opcional)',
        }
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre *',
            'slug': 'Slug *',
            'sitio_web': 'Sitio Web',
            'categoria': 'Categoría *',
        }

class MonedaForm(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = '__all__'
        labels = {
            'codigo': 'Código ISO *',
            'simbolo': 'Símbolo *',
            'decimales': 'Decimales *',
        }

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        labels = {
            'proveedor': 'Proveedor *',
            'nombre': 'Nombre del Plan *',
            'duracion_dias': 'Duración (días) *',
            'precio': 'Precio *',
            'moneda': 'Moneda *',
            'descripcion': 'Descripción (opcional)',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = '__all__'
        labels = {
            'tipo': 'Tipo *',
            'ultimos4': 'Últimos 4 Dígitos',
            'marca': 'Marca',
            'es_predeterminado': 'Predeterminado',
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        labels = {
            'suscripcion': 'Suscripción *',
            'texto': 'Comentario *',
        }
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3}),
        }