from django import forms
from .models import PostGato, PostPerro


class Perros_form(forms.ModelForm):
    class Meta:
        model = PostPerro
        fields = ['titulo', 'descripcion', 'fecha_recate', 'imagen']


class Gatos_form(forms.ModelForm):
    class Meta:
        model = PostGato
        fields = ['titulo', 'descripcion', 'fecha_recate', 'imagen']
