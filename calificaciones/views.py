from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Calificacion
from .forms import CalificacionForm
from suscripciones.models import Suscripcion
from django.db.models import Avg

class CalificacionListView(ListView):
    model = Calificacion
    template_name = "calificaciones/calificacion_list.html"
    context_object_name = "calificaciones"

    def get_queryset(self):
        self.suscripcion = get_object_or_404(Suscripcion, pk=self.kwargs["suscripcion_pk"])
        return Calificacion.objects.filter(suscripcion=self.suscripcion)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suscripcion"] = self.suscripcion
        context["promedio_puntuacion"] = Calificacion.objects.filter(suscripcion=self.suscripcion).aggregate(Avg('puntuacion'))['puntuacion__avg'] or "N/A"
        return context

class CalificacionCreateView(CreateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificaciones/calificacion_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.suscripcion = get_object_or_404(Suscripcion, pk=self.kwargs['suscripcion_pk'])
        obj.save()
        return redirect('calificaciones:list', suscripcion_pk=obj.suscripcion.pk)

class CalificacionUpdateView(UpdateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificaciones/calificacion_update.html'

    def get_success_url(self):
        return reverse_lazy('calificaciones:list', kwargs={'suscripcion_pk': self.object.suscripcion.pk})

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificaciones/calificacion_delete.html'

    def get_success_url(self):
        return reverse_lazy('calificaciones:list', kwargs={'suscripcion_pk': self.object.suscripcion.pk})