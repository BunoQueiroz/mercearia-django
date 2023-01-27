from django import forms
from user.models import User
from .utils import iterate_error_list
from user.forms.validators import login_validator

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Senha'
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        errors_list = {}
        login_validator(email, password, errors_list)

        iterate_error_list(errors_list, self)
        return self.cleaned_data
