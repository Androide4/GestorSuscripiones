from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
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
    logo = models.ImageField(upload_to='logos_proveedores/', blank=True, null=True, verbose_name="Logo")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
            original_slug = self.slug
            counter = 1
            while Proveedor.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


# Moneda (USD, COP, EUR, GBP, etc.)
class Moneda(models.Model):
    codigo = models.CharField(max_length=3, unique=True, verbose_name="Código ISO")
    simbolo = models.CharField(max_length=5, blank=True, verbose_name="Símbolo")
    decimales = models.PositiveSmallIntegerField(default=2, verbose_name="Decimales")
    ultima_actualizacion = models.DateTimeField(null=True, blank=True, verbose_name="Última actualización")

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


# Método de pago tokenizado (global, sin usuario)
class MetodoPago(models.Model):
    TIPO_CHOICES = [
        ('tarjeta', 'Tarjeta'),
        ('billetera', 'Billetera'),
        ('cuenta_bancaria', 'Cuenta bancaria'),
        ('otro', 'Otro'),
    ]

    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, verbose_name="Tipo")
    token = models.CharField(max_length=255, help_text="Token del gateway", verbose_name="Token")
    ultimos4 = models.CharField(max_length=4, blank=True, null=True, verbose_name="Últimos 4 dígitos")
    marca = models.CharField(max_length=50, blank=True, null=True, verbose_name="Marca")
    es_predeterminado = models.BooleanField(default=False, verbose_name="Predeterminado")
    metadatos = models.JSONField(blank=True, null=True, verbose_name="Datos adicionales")
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
    id_externo = models.CharField(
        max_length=255, blank=True, null=True, help_text="ID en el gateway externo", verbose_name="ID externo"
    )
    metadatos = models.JSONField(blank=True, null=True, verbose_name="Datos adicionales")
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
        if self.fecha_fin <= self.fecha_inicio:
            from django.core.exceptions import ValidationError
            raise ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

    def save(self, *args, **kwargs):
        if self.plan and not self.pk:
            self.fecha_fin = self.fecha_inicio + timezone.timedelta(days=self.plan.duracion_dias)
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.proveedor} ({self.get_estado_display()})"


# Pago realizado o intento
class Pago(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('fallido', 'Fallido'),
        ('reembolsado', 'Reembolsado'),
    ]

    suscripcion = models.ForeignKey(
        Suscripcion, on_delete=models.CASCADE, related_name="pagos", null=True, blank=True, verbose_name="Suscripción"
    )
    metodo_pago = models.ForeignKey(
        MetodoPago, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Método de pago"
    )
    monto = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Monto"
    )
    moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT, verbose_name="Moneda")
    tasa_cambio = models.DecimalField(
        max_digits=18, decimal_places=8, null=True, blank=True,
        help_text="Tasa usada para conversión", verbose_name="Tasa de cambio"
    )
    comision = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Comisión"
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    referencia = models.CharField(
        max_length=255, blank=True, null=True, help_text="ID de transacción", verbose_name="Referencia"
    )
    respuesta_gateway = models.JSONField(blank=True, null=True, verbose_name="Respuesta del gateway")
    pagado_en = models.DateTimeField(null=True, blank=True, verbose_name="Pagado en")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        indexes = [
            models.Index(fields=['referencia']),
            models.Index(fields=['estado']),
        ]
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.monto} {self.moneda} ({self.get_estado_display()})"


# Notificación programada
class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('recordatorio_vencimiento', 'Recordatorio de vencimiento'),
        ('pago_fallido', 'Pago fallido'),
        ('pago_exitoso', 'Pago exitoso'),
        ('manual', 'Manual'),
    ]

    suscripcion = models.ForeignKey(
        Suscripcion, on_delete=models.CASCADE, null=True, blank=True, related_name="notificaciones", verbose_name="Suscripción"
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name="Tipo")
    enviar_en = models.DateTimeField(verbose_name="Enviar en")
    enviado_en = models.DateTimeField(null=True, blank=True, verbose_name="Enviado en")
    datos = models.JSONField(blank=True, null=True, help_text="Datos para plantilla", verbose_name="Datos")
    leida = models.BooleanField(default=False, verbose_name="Leída")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        indexes = [
            models.Index(fields=['enviar_en']),
            models.Index(fields=['enviado_en']),
        ]
        ordering = ['-enviar_en']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.enviar_en}"


# Comentario en suscripción
class Comentario(models.Model):
    suscripcion = models.ForeignKey(
        Suscripcion, on_delete=models.CASCADE, related_name="comentarios", verbose_name="Suscripción"
    )
    texto = models.TextField(verbose_name="Comentario")
    metadatos = models.JSONField(blank=True, null=True, verbose_name="Datos adicionales")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-creado_en']

    def __str__(self):
        return f"Comentario en {self.suscripcion}"