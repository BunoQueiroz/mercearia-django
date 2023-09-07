from django.shortcuts import render
from django.contrib import auth
from core.views.utils import message_success_and_redirect, get_client_authenticated
from user.forms import LoginForm

def login(request):
    if request.user.is_authenticated:
        return login_client_or_404(request)
    form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def login_client(request):
    form = LoginForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        return login_client_or_404(request)
    return render(request, 'user/login.html', {'form': form})

def login_client_or_404(request):
    client = get_client_authenticated(request)
    auth.login(request, client)
    return message_success_and_redirect(request, 'Login realizado com sucesso', 'dashboard')

