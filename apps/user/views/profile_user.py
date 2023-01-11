from django.shortcuts import render, redirect
from user.models import Client
from core.views.utils import message_error_and_redirect, message_success_and_redirect, get_field_serialized

def profile(request):
    if request.user.is_authenticated:
        client = get_client(request)
        context = {'client': client}
        return render(request, 'user/profile.html', context)
    return redirect('home')

def update_profile(request):
    if request.method == 'POST' and request.user.is_authenticated:
        client = get_client(request)
        set_all_fields_client(request, client)    
        save_client_or_404(request, client)
    return redirect('profile')

def set_image_client(request, client):
    if 'img' in request.FILES:
        img = request.FILES['img']
        client.image = img # type: ignore

def get_client(request):
    possible_client = request.user.username
    client = Client.objects.filter(username=possible_client).get()
    return client

def save_client_or_404(request, client):
    try:
        client.save()
    except:
        return message_error_and_redirect(request, 'Usuário ou Email Inválido', 'profile')
    message_success_and_redirect(request, 'Dados alterados com sucesso', 'profile')

def set_all_fields_client(request, client):
    set_image_client(request, client)
    client.first_name = get_field_serialized(request, 'firstName')
    client.last_name = get_field_serialized(request, 'lastName')
    client.email = get_field_serialized(request, 'email')
    client.username = get_field_serialized(request, 'username')
