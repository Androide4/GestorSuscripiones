from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum
from django.utils import timezone
from .models import Suscripcion 
from .forms import SuscripcionForm

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
        context['monthly_spend'] = monthly_spend
        context['yearly_spend'] = yearly_spend
        context['active_subs'] = active_subs
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

    def get_object(self, queryset=None):
        return get_object_or_404(Suscripcion, pk=self.kwargs['pk'])