from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from suscripciones.models import Suscripcion, Proveedor, Moneda
from .models import Calificacion
from .forms import CalificacionForm

# ==================== TESTS DE MODELOS ====================
class CalificacionModelTest(TestCase):
    def setUp(self):
        proveedor = Proveedor.objects.create(nombre="Netflix", categoria="streaming")
        moneda = Moneda.objects.create(codigo="USD", simbolo="$")
        self.suscripcion = Suscripcion.objects.create(
            proveedor=proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            moneda=moneda,
            estado="activa"
        )

    def test_calificacion_creation(self):
        cal = Calificacion.objects.create(
            suscripcion=self.suscripcion,
            comentario="Muy bueno",
            puntuacion=9
        )
        self.assertEqual(cal.puntuacion, 9)

    def test_calificacion_str(self):
        cal = Calificacion.objects.create(suscripcion=self.suscripcion, puntuacion=7)
        self.assertIn("Netflix", str(cal))

    def test_clean_puntuacion_invalida(self):
        cal = Calificacion(suscripcion=self.suscripcion, puntuacion=11)
        with self.assertRaisesMessage(Exception, "La puntuación debe ser entre 1 y 10."):
            cal.clean()

# ==================== TESTS DE FORMULARIOS ====================
class CalificacionFormTest(TestCase):
    def test_form_valid(self):
        form = CalificacionForm(data={'comentario': 'Genial', 'puntuacion': 8})
        self.assertTrue(form.is_valid())

    def test_form_invalid_puntuacion_mayor_10(self):
        form = CalificacionForm(data={'puntuacion': 15})
        self.assertFalse(form.is_valid())

    def test_form_invalid_puntuacion_menor_1(self):
        form = CalificacionForm(data={'puntuacion': 0})
        self.assertFalse(form.is_valid())

# ==================== TESTS DE VISTAS ====================
class CalificacionViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        proveedor = Proveedor.objects.create(nombre="Disney", categoria="streaming")
        moneda = Moneda.objects.create(codigo="USD", simbolo="$")
        self.suscripcion = Suscripcion.objects.create(
            proveedor=proveedor,
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            moneda=moneda
        )
        self.calificacion = Calificacion.objects.create(
            suscripcion=self.suscripcion,
            comentario="Excelente",
            puntuacion=10
        )

    def test_list_view(self):
        url = reverse('calificaciones:list', kwargs={'suscripcion_pk': self.suscripcion.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "10")

    def test_create_view_get(self):
        url = reverse('calificaciones:create', kwargs={'suscripcion_pk': self.suscripcion.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_post(self):
        url = reverse('calificaciones:create', kwargs={'suscripcion_pk': self.suscripcion.pk})
        response = self.client.post(url, {'comentario': 'Buena', 'puntuacion': 7})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Calificacion.objects.filter(puntuacion=7).exists())