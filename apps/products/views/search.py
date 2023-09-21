from django.shortcuts import render, redirect
from products.models import Product
from core.views.utils import get_search_field_serialized, message_error_and_redirect

def search(request):
    if 'search' in request.GET and request.user.is_authenticated:
        return result_or_none(request)
    return redirect('home')

def result_or_none(request):
    search = get_search_field_serialized(request, 'search')
    products = Product.objects.filter(name__icontains=search, publicated=True)
    return render_with_filter(request, products, 'products')

def render_with_filter(request, search, name_in_template):
    if search.exists():
        context = {f'{name_in_template}': search}
        return render(request, 'products/product_search.html', context)
    return message_error_and_redirect(request, 'Infelizmente ainda não trabalhamos com esse produto', 'dashboard')
