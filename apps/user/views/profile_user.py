from django.shortcuts import render, redirect
from core.views.utils import message_success_and_redirect, get_field_serialized, get_object_client, message_error_and_redirect
from user.forms import UpdateClientForm, ChangePasswordForm
from django.db.utils import IntegrityError

def profile(request):
    if request.user.is_authenticated:
        client = get_object_client(request)
        context = create_context_profile(user=client, email_client=client.email)
        return render(request, 'user/profile.html', context)
    return redirect('home')

def update_profile(request):
    form = UpdateClientForm(request.POST)
    client = get_object_client(request)
    if request.method == 'POST' and form.is_valid():
        set_all_fields_client(request, client)    
        return save_client(request, client)
    context = create_context_profile(data_form=request.POST, email_client=client.email)
    return render(request, 'user/profile.html', context)

def set_image_client(request, client):
    if 'image' in request.FILES:
        img = request.FILES['image']
        client.image = img # type: ignore
    if request.POST.get('image-clear') == 'on':
        client.image = None

def create_context_profile(data_form=None, user=None, data_password=None, email_client=None):
    form = UpdateClientForm(data=data_form, instance=user)
    change_password = ChangePasswordForm(data=data_password, initial={'email': email_client})
    context = {
        'form': form,
        'change_password': change_password,
    }
    return context

def save_client(request, client):
    try:
        client.save()
        return message_success_and_redirect(request, 'Dados alterados com sucesso', 'profile')
    except IntegrityError:
        return message_error_and_redirect(request, 'Usuário Inválido', 'profile')

def set_all_fields_client(request, client):
    set_image_client(request, client)
    client.first_name = get_field_serialized(request, 'first_name')
    client.last_name = get_field_serialized(request, 'last_name')
    client.email = get_field_serialized(request, 'email')
    client.username = get_field_serialized(request, 'username')
