from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# Proveedor (Falabella, HBO, Netflix, etc.)
class Proveedor(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")
    sitio_web = models.URLField(blank=True, null=True, verbose_name="Sitio web")
    categoria = models.CharField(
        max_length=50,
        blank=True,
        choices=[
            ('retail', 'Retail'),
            ('streaming', 'Streaming'),
            ('software', 'Software'),
            ('educacion', 'Educación'),
            ('otros', 'Otros'),
        ],
        verbose_name="Categoría"
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Moneda (USD, COP, EUR, GBP, etc.)
class Moneda(models.Model):
    codigo = models.CharField(max_length=3, unique=True, verbose_name="Código ISO")
    simbolo = models.CharField(max_length=5, blank=True, verbose_name="Símbolo")
    decimales = models.PositiveSmallIntegerField(default=2, verbose_name="Decimales")

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} {self.simbolo}".strip()


# Plan predefinido de un proveedor
class Plan(models.Model):
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, related_name="planes", verbose_name="Proveedor"
    )
    nombre = models.CharField(max_length=120, verbose_name="Nombre del plan")
    duracion_dias = models.PositiveIntegerField(
        help_text="Duración en días (ej. 30 para mensual, 365 para anual)",
        verbose_name="Duración (días)"
    )
    precio = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio"
    )
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT, verbose_name="Moneda")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"
        unique_together = (('proveedor', 'nombre'),)
        ordering = ['proveedor__nombre', 'precio']

    def __str__(self):
        return f"{self.proveedor.nombre} - {self.nombre}"


# Método de pago (descriptivo, global)
class MetodoPago(models.Model):
    TIPO_CHOICES = [
        ('tarjeta', 'Tarjeta'),
        ('billetera', 'Billetera'),
        ('cuenta_bancaria', 'Cuenta bancaria'),
        ('otro', 'Otro'),
    ]

    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, verbose_name="Tipo")
    ultimos4 = models.CharField(max_length=4, blank=True, null=True, verbose_name="Últimos 4 dígitos")
    marca = models.CharField(max_length=50, blank=True, null=True, verbose_name="Marca")
    es_predeterminado = models.BooleanField(default=False, verbose_name="Predeterminado")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Método de pago"
        verbose_name_plural = "Métodos de pago"
        ordering = ['-es_predeterminado', 'creado_en']

    def save(self, *args, **kwargs):
        if self.es_predeterminado:
            MetodoPago.objects.filter(es_predeterminado=True).update(es_predeterminado=False)
        super().save(*args, **kwargs)

    def __str__(self):
        default = " (predeterminado)" if self.es_predeterminado else ""
        return f"{self.get_tipo_display()}{default}"


# Suscripción principal
class Suscripcion(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('pausada', 'Pausada'),
        ('cancelada', 'Cancelada'),
        ('vencida', 'Vencida'),
    ]

    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT, related_name="suscripciones", verbose_name="Proveedor"
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.SET_NULL, null=True, blank=True, related_name="suscripciones", verbose_name="Plan"
    )
    fecha_inicio = models.DateTimeField(default=timezone.now, verbose_name="Fecha de inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha de fin")
    renovacion_automatica = models.BooleanField(default=False, verbose_name="Renovación automática")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activa', verbose_name="Estado")
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT, verbose_name="Moneda")
    descripcion = models.TextField(
        blank=True, null=True, help_text="Motivo o detalles de la suscripción", verbose_name="Descripción"
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
        indexes = [
            models.Index(fields=['estado']),
            models.Index(fields=['fecha_fin']),
        ]
        ordering = ['-fecha_fin']

    def clean(self):
        # Validación segura: solo se ejecuta si ambos campos están presentes
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_fin <= self.fecha_inicio:
                raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

    def save(self, *args, **kwargs):
        if self.plan and not self.pk:
            self.fecha_fin = self.fecha_inicio + timezone.timedelta(days=self.plan.duracion_dias)
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.proveedor} ({self.get_estado_display()})"


# Comentario en suscripción
class Comentario(models.Model):
    suscripcion = models.ForeignKey(
        Suscripcion, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Suscripción"
    )
    texto = models.TextField(verbose_name="Comentario")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-creado_en']

    def __str__(self):
        return f"Comentario en {self.suscripcion}"