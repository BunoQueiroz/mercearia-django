from django.shortcuts import render
from products.models import Product
from django.contrib import messages

def search(request):
    if 'search' in request.GET:
        search = request.GET.get('search').strip()
        products = Product.objects.filter(name__icontains=search)
        if products.exists():
            context = {'products': products}
            return render(request, 'products/product_search.html', context)
        messages.error(request, 'Infelizmente ainda não trabalhamos com esse produto')
        return render(request, 'products/product_search.html')
