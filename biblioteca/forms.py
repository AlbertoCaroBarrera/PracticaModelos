
from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime
#from bootstrap_datepicker_plus.widgets import DatePickerInput

class LibroForm(forms.Form):
    nombre = forms.CharField(label="Nombre",
                             required=True,
                             max_length=200,
                             help_text="200 caracteres como maximo")
    
    descripcion = forms.CharField(label="Descripcion",
                                  required = False,
                                  widget=forms.Textarea())
    
    fecha_publicacion = forms.DateField(label="Fecha de publicación",
                                        initial=datetime.date.today,
                                        widget=forms.SelectDateWidget())
    
    idioma = forms.ChoiceField(choices=Libro.IDIOMAS,
                               initial="ES")
    
    bibliotecasDisponibles = Biblioteca.objects.all()
    biblioteca = forms.ModelChoiceField(
        queryset=bibliotecasDisponibles,
        widget=forms.Select,
        required=True,
        empty_label="Ninguna")
    
    autoresDisponibles = Autor.objects.all()
    autores = forms.ModelMultipleChoiceField(
        queryset=autoresDisponibles,
        required=True,
        help_text="Mantén pulsada la tecla control para seleccionar varios elementos"
        
    )