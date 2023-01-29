from django.shortcuts import redirect
from django.contrib import messages
from user.models import Client
from django.contrib import auth

def message_success_and_redirect(request, message, to_page):
    messages.success(request, message)
    return redirect(to_page)

def message_error_and_redirect(request, message, to_page):
    messages.error(request, message)
    return redirect(to_page)

def message_info_and_redirect(request, message, to_page):
    messages.info(request, message)
    return redirect(to_page)

def get_field_serialized(request, field):
    return str(request.POST.get(field)).strip()

def get_search_field_serialized(request, field):
    return str(request.GET.get(field)).strip()

def get_client_authenticated(request):
    password = get_field_serialized(request, 'password')
    email = get_field_serialized(request, 'email')
    username = Client.objects.filter(email=email).get().username
    client = auth.authenticate(request, username=username, password=password)
    if client is not None:
        return client

def get_object_client(request):
    return Client.objects.filter(username=request.user.username).get()
