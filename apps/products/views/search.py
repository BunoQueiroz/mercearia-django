from django.shortcuts import render, redirect
from products.models import Product
from django.contrib import messages

def search(request):
    if 'search' in request.GET:
        search = request.GET.get('search').strip()
        products = Product.objects.filter(name__icontains=search, publicated=True)
        if products.exists():
            context = {'products': products}
            return render(request, 'products/product_search.html', context)
        messages.error(request, 'Infelizmente ainda não trabalhamos com esse produto')
        return redirect('home')
    return redirect('home')
