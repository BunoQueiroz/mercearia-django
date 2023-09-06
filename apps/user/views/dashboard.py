from django.shortcuts import render, redirect
from user.models import Product
from core.views.utils import message_info_and_render

def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(publicated=True)
        return show_products_or_404(request, products)
    return redirect('home')

def show_products_or_404(request, products):
    if products.exists():
        return show_products(request, products)
    return message_info_and_render(
        request,
        'Infelizemente ainda não temos produtos disponíveis',
        'core/index.html'
        )

def show_products(request, products):
    context = {'products': products}
    return render(request, 'user/dashboard.html', context)
