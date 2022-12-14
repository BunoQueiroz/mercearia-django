from django.contrib import auth, messages
from django.shortcuts import redirect

def logout(request):
    messages.success(request, 'Logout realizado com sucesso')
    auth.logout(request)
    return redirect('home')
