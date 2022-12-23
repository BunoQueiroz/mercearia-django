from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('resgiter_user', register_user, name='register_user'),
    path('login_user', login_user, name='login_user'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('my_profile', profile, name='profile'),
    path('update_profile', update_profile, name='update_profile'),
    path('my_account', my_account, name='my_account'),
]
