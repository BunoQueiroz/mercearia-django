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
        if 'img' in request.FILES:
            set_image_client(request, client)

        client.first_name = first_name_serialized(request)
        client.last_name = last_name_serialized(request)
        client.email = email_serialized(request)
        client.username = username_serialized(request)
            
        save_client_or_404(request, client)
    return redirect('profile')


def first_name_serialized(request):
    return request.POST.get('firstName').strip()

def last_name_serialized(request):
    return request.POST.get('lastName').strip()

def email_serialized(request):
    return request.POST.get('email').strip()

def username_serialized(request):
    return request.POST.get('username').strip()

def set_image_client(request, client):
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
