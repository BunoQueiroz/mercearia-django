from django.shortcuts import render, get_object_or_404
from core.views.utils import get_field_serialized, get_object_client
from user.forms import ChangePasswordForm
from user.models import Client
from user.views.profile_user import save_client, create_context_profile
from django.contrib import messages

def set_password_client(request):
    form = ChangePasswordForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        return set_new_password(request)

    messages.error(request, 'Senha não alterada')
    user = get_object_or_404(Client, username=request.user.username)
    context = create_context_profile(request, initial={'email': user.email}, data=request.POST)
    return render(request, 'user/profile.html', context)

def set_new_password(request):
    client = get_object_client(request)
    new_password = get_field_serialized(request, 'new_password')
    client.set_password(new_password)
    return save_client(request, client)
