from django.urls import path
from .views import *

urlpatterns = [
    path('', all_products, name='all_products'),
    path('search', search, name='search'),
    path('landing_page/<int:product_id>', landing_page, name='landing_page'),
]
