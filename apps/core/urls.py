from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('send_message', send_by_email, name='send_message'),
]
