from django.urls import path
from .views import CalificacionListView, CalificacionCreateView, CalificacionUpdateView, CalificacionDeleteView

app_name = 'calificaciones'
urlpatterns = [
    path('suscripcion/<int:suscripcion_pk>/calificaciones/', CalificacionListView.as_view(), name='list'),
    path('suscripcion/<int:suscripcion_pk>/calificaciones/create/', CalificacionCreateView.as_view(), name='create'),
    path('calificaciones/<int:pk>/update/', CalificacionUpdateView.as_view(), name='update'),
    path('calificaciones/<int:pk>/delete/', CalificacionDeleteView.as_view(), name='delete'),
]