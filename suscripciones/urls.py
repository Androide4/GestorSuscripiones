from django.urls import path
from .views import SuscripcionListView, SuscripcionCreateView, SuscripcionUpdateView

app_name = 'suscripciones'
urlpatterns = [
    path('', SuscripcionListView.as_view(), name='list'),
    path('create/', SuscripcionCreateView.as_view(), name='create'),
    path('<int:pk>/update/', SuscripcionUpdateView.as_view(), name='update'),
]