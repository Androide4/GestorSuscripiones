from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['comentario', 'puntuacion']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
            'puntuacion': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
        labels = {
            'comentario': 'Comentario',
            'puntuacion': 'Puntuación',
        }