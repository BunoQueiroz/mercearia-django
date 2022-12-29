from django.shortcuts import render, redirect
from user.models import Product
from django.contrib import messages

def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(publicated=True)
        return show_products_or_404(request, products)
    return redirect('home')

def show_products_or_404(request, products):
    if products.exists():
        return show_products(request, products)
    return products_not_found(request)

def show_products(request, products):
    context = {'products': products}
    return render(request, 'user/dashboard.html', context)

def products_not_found(request):
    messages.info(request, 'Infelizemente ainda não temos produtos disponíveis')
    return render(request, 'user/dashboard.html')
