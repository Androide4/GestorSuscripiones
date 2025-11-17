from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import Suscripcion, Proveedor, Moneda, Plan, MetodoPago, Comentario
from .forms import SuscripcionForm, ProveedorForm, MonedaForm, PlanForm, MetodoPagoForm, ComentarioForm
from calificaciones.models import Calificacion
from django.db import models

# Suscripciones
class SuscripcionListView(ListView):
    model = Suscripcion
    template_name = 'suscripciones/suscripciones_list.html'
    context_object_name = 'suscripciones'

    def get_queryset(self):
        return Suscripcion.objects.filter(estado__in=['activa', 'pausada']).order_by('-fecha_fin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_subs = Suscripcion.objects.filter(estado='activa').count()
        monthly_spend = Suscripcion.objects.filter(estado='activa').aggregate(total=Sum('plan__precio'))['total'] or 0
        yearly_spend = monthly_spend * 12
        upcoming = Suscripcion.objects.filter(estado='activa').count()
        context['monthly_spend'] = monthly_spend
        context['yearly_spend'] = yearly_spend
        context['active_subs'] = active_subs
        context['upcoming'] = upcoming

        for sub in context['suscripciones']:
            avg = Calificacion.objects.filter(suscripcion=sub).aggregate(models.Avg('puntuacion'))['puntuacion__avg'] or "N/A"
            sub.avg_puntuacion = avg

        return context

class SuscripcionCreateView(CreateView):
    model = Suscripcion
    form_class = SuscripcionForm
    template_name = 'suscripciones/suscripcion_create.html'
    success_url = reverse_lazy('suscripciones:list')

class SuscripcionUpdateView(UpdateView):
    model = Suscripcion
    form_class = SuscripcionForm
    template_name = 'suscripciones/suscripcion_update.html'
    success_url = reverse_lazy('suscripciones:list')

    def get_object(self):
        return get_object_or_404(Suscripcion, pk=self.kwargs['pk'])

class SuscripcionDeleteView(DeleteView):
    model = Suscripcion
    template_name = 'suscripciones/suscripcion_delete.html'
    success_url = reverse_lazy('suscripciones:list')

# Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'suscripciones/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'suscripciones/proveedor_create.html'
    success_url = reverse_lazy('suscripciones:proveedores_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'suscripciones/proveedor_update.html'
    success_url = reverse_lazy('suscripciones:proveedores_list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'suscripciones/proveedor_delete.html'
    success_url = reverse_lazy('suscripciones:proveedores_list')

# Monedas (similar, ajusta template names)
class MonedaListView(ListView):
    model = Moneda
    template_name = 'suscripciones/moneda_list.html'
    context_object_name = 'monedas'

class MonedaCreateView(CreateView):
    model = Moneda
    form_class = MonedaForm
    template_name = 'suscripciones/moneda_create.html'
    success_url = reverse_lazy('suscripciones:monedas_list')

class MonedaUpdateView(UpdateView):
    model = Moneda
    form_class = MonedaForm
    template_name = 'suscripciones/moneda_update.html'
    success_url = reverse_lazy('suscripciones:monedas_list')

class MonedaDeleteView(DeleteView):
    model = Moneda
    template_name = 'suscripciones/moneda_delete.html'
    success_url = reverse_lazy('suscripciones:monedas_list')

# Planes
class PlanListView(ListView):
    model = Plan
    template_name = 'suscripciones/plan_list.html'
    context_object_name = 'planes'

class PlanCreateView(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'suscripciones/plan_create.html'
    success_url = reverse_lazy('suscripciones:planes_list')

class PlanUpdateView(UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = 'suscripciones/plan_update.html'
    success_url = reverse_lazy('suscripciones:planes_list')

class PlanDeleteView(DeleteView):
    model = Plan
    template_name = 'suscripciones/plan_delete.html'
    success_url = reverse_lazy('suscripciones:planes_list')

# Métodos de Pago
class MetodoPagoListView(ListView):
    model = MetodoPago
    template_name = 'suscripciones/metodo_pago_list.html'
    context_object_name = 'metodos_pago'

class MetodoPagoCreateView(CreateView):
    model = MetodoPago
    form_class = MetodoPagoForm
    template_name = 'suscripciones/metodo_pago_create.html'
    success_url = reverse_lazy('suscripciones:metodos_pago_list')

class MetodoPagoUpdateView(UpdateView):
    model = MetodoPago
    form_class = MetodoPagoForm
    template_name = 'suscripciones/metodo_pago_update.html'
    success_url = reverse_lazy('suscripciones:metodos_pago_list')

class MetodoPagoDeleteView(DeleteView):
    model = MetodoPago
    template_name = 'suscripciones/metodo_pago_delete.html'
    success_url = reverse_lazy('suscripciones:metodos_pago_list')

# Comentarios
class ComentarioListView(ListView):
    model = Comentario
    template_name = 'suscripciones/comentario_list.html'
    context_object_name = 'comentarios'

class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'suscripciones/comentario_create.html'
    success_url = reverse_lazy('suscripciones:comentarios_list')

class ComentarioUpdateView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'suscripciones/comentario_update.html'
    success_url = reverse_lazy('suscripciones:comentarios_list')

class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'suscripciones/comentario_delete.html'
    success_url = reverse_lazy('suscripciones:comentarios_list')