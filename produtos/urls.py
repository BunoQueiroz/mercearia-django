from django.urls import path
from produtos.views import index

urlpatterns = [
    path('', index, name='index')
]