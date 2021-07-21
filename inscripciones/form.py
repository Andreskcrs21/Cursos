from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from  .models import Inscripcion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
        
            

        ]
        labels = {
            'username': 'Nombre de usuario',
            

        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
    
        fields = ('fecha_inscripcion', 'curso', 'costo_total')

