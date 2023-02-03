from django import forms
from .utils import iterate_error_list
from user.models import Client
from core.validators import non_numeric_field

class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['image', 'first_name', 'last_name', 'username', 'email']
        labels = {
            'image': 'Alterar foto de perfil',
            'first_name': 'Seu nome',
            'last_name': 'Seu sobrenome',
            'username': 'Nome de usuário',
            'email': 'Email'
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={ 'placeholder': 'Seu nome', 'class': 'form-control fw-semibold mt-2'}),
            'first_name': forms.TextInput(attrs={ 'placeholder': 'Seu nome', 'class': 'form-control fw-semibold'}),
            'last_name': forms.TextInput(attrs={ 'placeholder': 'Seu sobrenome', 'class': 'form-control fw-semibold'}),
            'username': forms.TextInput(attrs={ 'placeholder': 'Nome de usuário', 'class': 'form-control fw-semibold'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu email', 'class': 'form-control fw-semibold'}),
        }

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        errors_list = {}
        non_numeric_field(first_name, 'first_name', errors_list)
        non_numeric_field(last_name, 'last_name', errors_list)
        iterate_error_list(errors_list, self)
        
        return self.cleaned_data
