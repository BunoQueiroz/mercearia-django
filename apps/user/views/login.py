from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    return render(request, 'user/login.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_data = User.objects

        if user_data.filter(email=email).exists():
            username = user_data.get(email=email)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                return login_client(request, user)
            return fail_login(request)
        return email_not_found(request)
    return redirect('login')

def email_not_found(request):
    messages.error(request, 'Email não cadastrado')
    return redirect('login')

def fail_login(request):
    messages.error(request, 'Credenciais não reconhecidas')
    return redirect('login')

def login_client(request, client):
    auth.login(request, client)
    messages.success(request, 'Login realizado com sucesso')
    return redirect('dashboard')
