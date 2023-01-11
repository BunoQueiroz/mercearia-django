from django.shortcuts import redirect
from user.models import Client
from django.contrib.auth import authenticate
from core.views.utils import message_error_and_redirect, message_success_and_redirect

def set_password_client(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('confirmNewPassword')
        return invalid_passwords_or_set(request, current_password, new_password, confirm_new_password)
    return redirect('profile')

def set_new_password_or_404(request, current_password, new_password):
    if authenticator_client(request, current_password):
        client = get_client_authenticated(request)
        set_new_password_and_save(client, new_password)
        return message_success_and_redirect(request, 'Senha alterada com sucesso', 'login')
    return message_error_and_redirect(request, 'Senha atual incorreta', 'profile')

def authenticator_client(request, current_password):
    client = get_client_authenticated(request)
    user = authenticate(username=client.username, password=current_password)
    if user is not None:
        return True
    return False

def get_client_authenticated(request):
    return Client.objects.filter(username=request.user.username).get()

def set_new_password_and_save(client, new_password):
    client.set_password(str(new_password))
    client.save()

def invalid_passwords_or_set(request, current_password, new_password, confirm_new_password):
    if new_password != confirm_new_password or len(str(new_password)) < 8:
        return message_error_and_redirect(request, 'Por favor revise sua nova senha', 'profile')
    return set_new_password_or_404(request, current_password, new_password)
