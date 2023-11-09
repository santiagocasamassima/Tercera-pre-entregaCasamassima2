from django import forms

class EquipoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    descripcion = forms.CharField(required=True, max_length=50000) 
    ubicacion = forms.CharField(required=True, max_length=256)