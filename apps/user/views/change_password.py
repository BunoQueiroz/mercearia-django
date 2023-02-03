from django.shortcuts import render
from core.views.utils import get_field_serialized, get_object_client
from user.forms import ChangePasswordForm
from user.views.profile_user import save_client, create_context_profile
from django.contrib import messages

def set_password_client(request):
    form = ChangePasswordForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        return set_new_password(request)

    messages.error(request, 'Senha não alterada')
    client = get_object_client(request)
    context = create_context_profile(user=client, email_client=client.email, data_password=request.POST)
    return render(request, 'user/profile.html', context)

def set_new_password(request):
    client = get_object_client(request)
    new_password = get_field_serialized(request, 'new_password')
    client.set_password(new_password)
    return save_client(request, client)
