from user.models import Client
from django import forms
from .utils import iterate_error_list
from core.validators import non_numeric_field
from user.forms.validators import password_validator, repeated_email

class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control fst-italic form-input fw-semibold'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control fst-italic form-input fw-semibold'}),
            'email': forms.EmailInput(attrs={'class': 'form-control fst-italic form-input fw-semibold'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control fst-italic form-input fw-semibold'}),
        }
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha'
        }
    confirm_password = forms.CharField(
        max_length=256, 
        required=True, 
        label='Confirmar Senha',
        widget=forms.PasswordInput(
            attrs={'class':'form-control fst-italic form-input fw-semibold'}
        )
    )

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        email = self.cleaned_data.get('email')
        errors_list = {}
        non_numeric_field(first_name, 'first_name', errors_list)
        non_numeric_field(last_name, 'last_name', errors_list)
        password_validator(password, confirm_password, errors_list)
        repeated_email(email, errors_list)

        iterate_error_list(errors_list, self)

        return self.cleaned_data
