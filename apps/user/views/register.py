from django.shortcuts import render, redirect
from .utils import message_success_and_redirect, message_error_and_redirect, get_field_serialized
from django.contrib.auth.models import User
from user.models import Client

def register(request):
    return render(request, 'user/register.html')

def register_client(request):
    if request.method == 'POST':
        return register_client_or_404(request)
    return redirect('register')

def register_client_or_404(request):
    email = get_field_serialized(request, 'email')
    password = get_field_serialized(request, 'password')
    confirm_password = get_field_serialized(request, 'confirmPassword')

    if(password != confirm_password or len(str(password)) < 8 or User.objects.filter(email=email).exists()):
        return message_error_and_redirect(request, 'Por favor, verifique sua senha, ou insira um email válido', 'register')
    
    first_name = get_field_serialized(request, 'name')
    last_name = get_field_serialized(request, 'lastName')

    Client.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=False)
    return message_success_and_redirect(request, 'Cadastro realizado com sucesso', 'login')
