from django.shortcuts import render, redirect
from user.models import Product

def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(publicated=True)
        if products.exists():
            context = {'products': products}
            return render(request, 'user/dashboard.html', context)
    return redirect('home')
