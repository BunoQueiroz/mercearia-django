from django import forms
from core.validators import *
from core.models import Contact
from user.forms.utils import iterate_error_list

class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control fw-semibold text-primary fs-5 py-0'}),
            'email': forms.EmailInput(attrs={'class':'form-control fw-semibold text-primary fs-5 py-0'}),
            'phone': forms.TextInput(attrs={'class':'form-control fw-semibold text-primary fs-5 py-0'}),
            'message': forms.Textarea(attrs={'class':'form-control fw-semibold text-primary fs-5 py-0'}),
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

        iterate_error_list(errors_list, self)
        return self.cleaned_data
