from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from core.views.utils import message_error_and_redirect, message_success_and_redirect, get_field_serialized

def login(request):
    return render(request, 'user/login.html')

def login_client(request):
    if request.method == 'POST':
        email = get_field_serialized(request, 'email')
        password = get_field_serialized(request, 'password')
        return login_client_if_exists(request, email, password)
    return redirect('login')

def login_client_or_404(request, user):
    if user is not None:
        auth.login(request, user)
        return message_success_and_redirect(request, 'Login realizado com sucesso', 'dashboard')
    return message_error_and_redirect(request, 'Credenciais não reconhecidas', 'login')

def login_client_if_exists(request, email, password):
    users_data = User.objects
    if users_data.filter(email=email).exists():
        username = users_data.get(email=email)
        user = auth.authenticate(username=username, password=password)
        return login_client_or_404(request, user)
    return message_error_and_redirect(request, 'Email não cadastrado', 'login')
