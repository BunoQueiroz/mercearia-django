from django import forms
from user.models import Client
from user.forms.validators import password_validator, current_password_validator
from user.forms.utils import iterate_error_list

class ChangePasswordForm(forms.ModelForm):
    new_password = forms.CharField(
        min_length=8,
        label='Nova Senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control fw-semibold text-primary fs-5 py-0'}
        )
    )
    confirm_password = forms.CharField(
        min_length=8,
        label= 'Confirme Sua Nova Senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control fw-semibold text-primary fs-5 py-0'}
        )
    )
    class Meta:
        model = Client
        fields = ['password', 'email']
        labels = {
            'password': 'Senha atual',
            'email': ''
        }
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'd-none'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control fw-semibold text-primary fs-5 py-0'}
            )
        }
    
    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        errors_list = {}
        password_validator(new_password, confirm_password, errors_list)
        current_password_validator(password, email, errors_list)

        iterate_error_list(errors_list, self)
        return self.cleaned_data
