from django.shortcuts import redirect
from user.models import Client
from django.contrib.auth import authenticate
from django.contrib import messages

def set_password_client(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('confirmNewPassword')

        if new_password != confirm_new_password or len(str(new_password)) < 8:
            return different_passwords(request)
        
        client = Client.objects.filter(username=request.user.username).get()
        user = authenticate(username=client.username, password=current_password)
        if user is not None:
            client.set_password(str(new_password))
            client.save()
            return success_set_password(request)

        return fail_set_password(request)
    return redirect('profile')

def different_passwords(request):
    messages.error(request, 'Por favor revise sua nova senha')
    return redirect('profile')

def success_set_password(request):
    messages.success(request, 'Senha alterada com sucesso')
    return redirect('login')

def fail_set_password(request):
    messages.error(request, 'Cliente não encontrado')
    return redirect('profile')
