from django.shortcuts import render
from core.views.utils import message_success_and_redirect, get_field_serialized
from user.models import Client
from user.forms import ClientRegisterForm

def register(request):
    form = ClientRegisterForm()
    return render(request, 'user/register.html', context={'form': form})

def register_client(request):
    form = ClientRegisterForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        return try_register_client(request)
    return render(request, 'user/register.html', {'form': form})

def try_register_client(request):
    email = get_field_serialized(request, 'email')
    password = get_field_serialized(request, 'password')
    first_name = get_field_serialized(request, 'first_name')
    last_name = get_field_serialized(request, 'last_name')

    Client.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=False)
    return message_success_and_redirect(request, 'Cadastro realizado com sucesso', 'login')
