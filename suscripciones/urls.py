from django.urls import path
from .views import (
    SuscripcionListView, SuscripcionCreateView, SuscripcionUpdateView, SuscripcionDeleteView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    MonedaListView, MonedaCreateView, MonedaUpdateView, MonedaDeleteView,
    PlanListView, PlanCreateView, PlanUpdateView, PlanDeleteView,
    MetodoPagoListView, MetodoPagoCreateView, MetodoPagoUpdateView, MetodoPagoDeleteView,
    ComentarioListView, ComentarioCreateView, ComentarioUpdateView, ComentarioDeleteView
)

app_name = 'suscripciones'
urlpatterns = [
    # Principal (Suscripciones)
    path('', SuscripcionListView.as_view(), name='list'),
    path('create/', SuscripcionCreateView.as_view(), name='create'),
    path('<int:pk>/update/', SuscripcionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', SuscripcionDeleteView.as_view(), name='delete'),

    # Proveedores
    path('proveedores/', ProveedorListView.as_view(), name='proveedores_list'),
    path('proveedores/create/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/update/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedores/<int:pk>/delete/', ProveedorDeleteView.as_view(), name='proveedor_delete'),

    # Monedas
    path('monedas/', MonedaListView.as_view(), name='monedas_list'),
    path('monedas/create/', MonedaCreateView.as_view(), name='moneda_create'),
    path('monedas/<int:pk>/update/', MonedaUpdateView.as_view(), name='moneda_update'),
    path('monedas/<int:pk>/delete/', MonedaDeleteView.as_view(), name='moneda_delete'),

    # Planes
    path('planes/', PlanListView.as_view(), name='planes_list'),
    path('planes/create/', PlanCreateView.as_view(), name='plan_create'),
    path('planes/<int:pk>/update/', PlanUpdateView.as_view(), name='plan_update'),
    path('planes/<int:pk>/delete/', PlanDeleteView.as_view(), name='plan_delete'),

    # Métodos de Pago
    path('metodos-pago/', MetodoPagoListView.as_view(), name='metodos_pago_list'),
    path('metodos-pago/create/', MetodoPagoCreateView.as_view(), name='metodo_pago_create'),
    path('metodos-pago/<int:pk>/update/', MetodoPagoUpdateView.as_view(), name='metodo_pago_update'),
    path('metodos-pago/<int:pk>/delete/', MetodoPagoDeleteView.as_view(), name='metodo_pago_delete'),

    # Comentarios
    path('comentarios/', ComentarioListView.as_view(), name='comentarios_list'),
    path('comentarios/create/', ComentarioCreateView.as_view(), name='comentario_create'),
    path('comentarios/<int:pk>/update/', ComentarioUpdateView.as_view(), name='comentario_update'),
    path('comentarios/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario_delete'),
]