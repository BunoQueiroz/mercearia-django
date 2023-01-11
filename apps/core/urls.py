from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_message', views.send_by_email, name='send_message'),
]
