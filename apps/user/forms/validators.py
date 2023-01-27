from user.models import Client
from django.contrib import auth

def password_validator(password, confirm_password, errors_list):
    password_short(password, errors_list)
    different_passwords(password, confirm_password, errors_list)

def password_short(password, errors_list):
    if len(str(password)) < 8:
        errors_list['password'] = 'Sua senha está muito curta. Use pelo menos 8 dígitos'

def different_passwords(password, confirm_password, erros_list):
    if password != confirm_password:
        erros_list['confirm_password'] = 'Suas senhas estão diferentes'

def repeated_email(email, errors_list):
    mail = Client.objects.filter(email=email)
    if mail.exists():
        errors_list['email'] = 'Email já Cadastrado'

def login_validator(email, password, errors_list):
    mail = Client.objects.filter(email=email)
    if not mail.exists():
        errors_list['email'] = 'Email não Cadastrado'
        return

    user = Client.objects.get(email=email)
    client = auth.authenticate(username=user.username, password=password)
    if client is None:
        errors_list['password'] = 'Credenciais não reconhecidas'

