from django.shortcuts import render, get_list_or_404
from products.models import Product

def landing_page(request, product_id):
    product = get_list_or_404(Product, pk=product_id, publicated=True)[0]
    return render(request, 'products/landing_page.html', {'product': product})
