from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from random import randrange
def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']

        hash_str = str(randrange(1111, 99999))

        user = User.objects.create_user(is_superuser=False, username=first_name + hash_str, first_name=first_name, last_name=last_name, email=email, password=password)
        
        user.save()

        messages.success(request, 'Cadastro realizado com Sucesso')
        return redirect('login')
