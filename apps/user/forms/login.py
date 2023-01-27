from django import forms
from user.models import User
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

        if errors_list is not None:
            for error in errors_list:
                message_error = errors_list[error]
                self.add_error(error, message_error)
        return self.cleaned_data
