from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from random import randrange

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def register_user(request):

    def data_invalid():
        return (password != confirm_password or User.objects.filter(email=email).exists() or len(str(password)) < 8)

    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']


        if( data_invalid() ):
            current_page = 'register'
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Este Email ja está cadastrado em nosso sistema')

            if len(str(password)) < 8:
                messages.error(request, 'A sua senha está muito fraca')
            
            if password != confirm_password:
                messages.error(request, 'As senhas informadas estavam diferente')
            messages.error(request, 'Não deu certo')
            return redirect(current_page)

        else:
            hash_str = str(randrange(1111, 99999))
            user_name = first_name + hash_str
            
            user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=False)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso')

            return redirect('login')
