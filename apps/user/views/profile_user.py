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
            img = request.FILES['img']
            client.image = img # type: ignore

        first_name_serialized = request.POST.get('firstName').strip()
        last_name_serialized = request.POST.get('lastName').strip()
        email_serialized = request.POST.get('email').strip()
        username_serialized = request.POST.get('username').strip()

        client.first_name = first_name_serialized
        client.last_name = last_name_serialized
        client.email = email_serialized
        client.username = username_serialized

        try:
            client.save()
        except:
            messages.error(request, 'Usuário ou Email Inválido')
            return redirect('profile')
            
        messages.success(request, 'Dados alterados com sucesso')
        return redirect('profile')

    return redirect('profile')

def get_client(request):
    possible_client = request.user.username
    client = Client.objects.filter(username=possible_client).get()
    return client
