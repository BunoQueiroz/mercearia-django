from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from user.models import Client

def register(request):
    return render(request, 'user/register.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if(password != confirm_password or len(str(password)) < 8 or User.objects.filter(email=email).exists()):
            return error_password_or_email(request)

        Client.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=False)
        return register_user_success(request)
        
    return redirect('register')

def register_user_success(request):
    messages.success(request, 'Cadastro realizado com sucesso')
    return redirect('login')

def error_password_or_email(request):
    messages.error(request, 'Por favor, verifique sua senha, ou insira um email válido')
    return redirect('register')
