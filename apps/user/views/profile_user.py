from django.shortcuts import render, redirect, get_object_or_404
from user.models import Client
from core.views.utils import message_success_and_redirect, get_field_serialized
from user.forms import UpdateClientForm

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = get_object_or_404(Client, username=username)
        form = UpdateClientForm(instance=user)
        context = {'form': form}
        return render(request, 'user/profile.html', context)
    return redirect('home')

def update_profile(request):
    form = UpdateClientForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        client = get_client(request)
        set_all_fields_client(request, client)    
        return save_client(request, client)
    return render(request, 'user/profil.html', {'form': form})

def set_image_client(request, client):
    if 'image' in request.FILES:
        img = request.FILES['image']
        client.image = img # type: ignore
    if request.POST.get('image-clear') == 'on':
        client.image = ''

def get_client(request):
    possible_client = request.user.username
    client = Client.objects.filter(username=possible_client).get()
    return client

def save_client(request, client):
    client.save()
    return message_success_and_redirect(request, 'Dados alterados com sucesso', 'profile')

def set_all_fields_client(request, client):
    set_image_client(request, client)
    client.first_name = get_field_serialized(request, 'first_name')
    client.last_name = get_field_serialized(request, 'last_name')
    client.email = get_field_serialized(request, 'email')
    client.username = get_field_serialized(request, 'username')
