from django import forms
from core.validators import *
from core.models import Contact

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(),
        }
        labels = {
            'full_name': 'Nome completo',
            'email': 'Email',
            'phone': 'Telefone',
            'message': 'Mensagem',
        }

    def clean(self):
        full_name = self.cleaned_data.get('full_name')
        phone = self.cleaned_data.get('phone')
        message = self.cleaned_data.get('message')
        errors_list = {}
        
        non_numeric_field(full_name, 'full_name', errors_list)
        phone_valid(phone, 'phone', errors_list)
        message_valid(message, 'message', errors_list)

        if errors_list is not None:
            for error in errors_list:
                message_error = errors_list[error]
                self.add_error(error, message_error)
        return self.cleaned_data
