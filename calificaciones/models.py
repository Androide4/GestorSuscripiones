from django.db import models
from django.core.exceptions import ValidationError
from suscripciones.models import Suscripcion

class Calificacion(models.Model):
    suscripcion = models.ForeignKey(
        Suscripcion,
        on_delete=models.CASCADE,
        related_name='calificaciones',
        verbose_name="Suscripción"
    )
    comentario = models.TextField("Comentario", blank=True, null=True)
    puntuacion = models.IntegerField("Puntuación")

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return f"{self.suscripcion} - {self.puntuacion}"

    def clean(self):
        if self.puntuacion < 1 or self.puntuacion > 10:
            raise ValidationError("La puntuación debe ser entre 1 y 10.")