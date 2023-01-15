from django import forms

class ContactForms(forms.Form):
    full_name = forms.CharField(max_length=100, label='Nome completo', required=True)
    email = forms.EmailField(max_length=100, label='Email', required=True)
    phone = forms.IntegerField(max_value=99999999999, min_value=11911111111, required=False)
    message = forms.CharField(
        max_length=256,
        widget=forms.Textarea(),
        label='Mensagem',
        required=True
    )
