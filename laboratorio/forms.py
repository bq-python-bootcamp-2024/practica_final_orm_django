from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput
from .models import Laboratorio

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        labels = {
            'nombre': _('Nombre'),
            # Migración 'actualizado_campos'
            'ciudad': _('Ciudad'),
            'pais': _('País'),
        }

        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese el nombre del laboratorio'}),
            # Migración 'actualizado_campos'
            'ciudad': TextInput(attrs={'placeholder': 'Ingrese la ciudad del laboratorio'}),
            'pais': TextInput(attrs={'placeholder': 'Ingrese el país del laboratorio'}),
        }