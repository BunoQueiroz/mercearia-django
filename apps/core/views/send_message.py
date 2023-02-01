from user.views.profile_user import get_field_serialized
from django.core.mail import send_mail
from .utils import message_error_and_redirect, message_success_and_redirect
from core.forms import ContactForms
from django.shortcuts import render

def send_by_email(request):
    form = ContactForms(request.POST)
    if request.method == "POST" and form.is_valid():
        return try_to_send_message(request)
    return render(request, 'core/contact.html', {'form': form})

def get_all_fields(request):
    name = get_field_serialized(request, 'name')
    email = get_field_serialized(request, 'email')
    wpp = get_field_serialized(request, 'whatsapp')
    message = get_field_serialized(request, 'message')
    dict_message = {
        'name': name,
        'email': email,
        'wpp': wpp,
        'message': message,
    }
    return dict_message
    
def try_to_send_message(request):
    fields = get_all_fields(request)
    try:
        send_message_for_mail(fields)
        return message_success_and_redirect(request, 'Mensagem enviada com sucesso', 'home')
    except:
        return message_error_and_redirect(request, 'Falha ao tentar enviar o email', 'home')

def send_message_for_mail(fields):
    send_mail(
        f'Mensagem de {fields.get("name")}',
        f'{fields.get("message")} \n\n Fone para contato: {fields.get("wpp")} \n email: {fields.get("email")}', 
        'user@gmail.com', 
        ['to@gmail.com'], 
        fail_silently=False
    )
