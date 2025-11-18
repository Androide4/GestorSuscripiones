from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Suscripcion, Proveedor, Moneda, Plan, MetodoPago
from .forms import SuscripcionForm

# ==================== TESTS DE MODELOS ====================
class SuscripcionModelTest(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(nombre="Netflix", categoria="streaming")
        self.moneda = Moneda.objects.create(codigo="USD", simbolo="$")

    def test_suscripcion_creation(self):
        sus = Suscripcion.objects.create(
            proveedor=self.proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            moneda=self.moneda,
            estado="activa"
        )
        self.assertEqual(sus.estado, "activa")

    def test_suscripcion_str(self):
        sus = Suscripcion.objects.create(
            proveedor=self.proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            moneda=self.moneda
        )
        self.assertIn("Netflix", str(sus))

    def test_clean_fecha_invalida(self):
        sus = Suscripcion(
            proveedor=self.proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() - timezone.timedelta(days=1),
            moneda=self.moneda
        )
        with self.assertRaisesMessage(Exception, "La fecha de fin debe ser posterior a la fecha de inicio"):
            sus.clean()

# ==================== TESTS DE FORMULARIOS ====================
class SuscripcionFormTest(TestCase):
    def setUp(self):
        Proveedor.objects.create(nombre="Test", categoria="streaming")
        Moneda.objects.create(codigo="USD", simbolo="$")

    def test_form_valid(self):
        data = {
            'proveedor': Proveedor.objects.first().pk,
            'fecha_inicio': timezone.now().date(),
            'fecha_fin': (timezone.now() + timezone.timedelta(days=30)).date(),
            'moneda': Moneda.objects.first().pk,
            'estado': 'activa'
        }
        form = SuscripcionForm(data=data)
        self.assertTrue(form.is_valid())
        
        def test_form_invalid_sin_campos(self):
            form = SuscripcionForm(data={})
            self.assertFalse(form.is_valid())
            self.assertTrue(any("required" in error.lower() for error in form.errors.as_text().splitlines()))
            self.assertIn("required", form.errors.as_text())

# ==================== TESTS DE VISTAS ====================
class SuscripcionViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.proveedor = Proveedor.objects.create(nombre="Spotify", categoria="musica")
        self.moneda = Moneda.objects.create(codigo="EUR", simbolo="€")
        self.suscripcion = Suscripcion.objects.create(
            proveedor=self.proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            moneda=self.moneda,
            estado="activa"
        )

    def test_list_view(self):
        response = self.client.get(reverse('suscripciones:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spotify")

    def test_create_view_get(self):
        response = self.client.get(reverse('suscripciones:create'))
        self.assertEqual(response.status_code, 200)

    def test_create_view_post(self):
        data = {
            'proveedor': self.proveedor.pk,
            'fecha_inicio': timezone.now().date(),
            'fecha_fin': (timezone.now() + timezone.timedelta(days=30)).date(),
            'moneda': self.moneda.pk,
            'estado': 'activa'
        }
        response = self.client.post(reverse('suscripciones:create'), data)
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Suscripcion.objects.count(), 2)