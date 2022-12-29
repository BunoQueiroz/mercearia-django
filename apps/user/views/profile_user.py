from django.shortcuts import render, redirect
from user.models import Client
from django.contrib import messages

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

def get_field_serialized(request, field):
    return request.POST.get(field).strip()

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
        messages.error(request, 'Usuário ou Email Inválido')
        return redirect('profile')
    success_update_client(request)

def success_update_client(request,):
    messages.success(request, 'Dados alterados com sucesso')
    return redirect('profile')

def set_all_fields_client(request, client):
    set_image_client(request, client)
    client.first_name = get_field_serialized(request, 'firstName')
    client.last_name = get_field_serialized(request, 'lastName')
    client.email = get_field_serialized(request, 'email')
    client.username = get_field_serialized(request, 'username')
