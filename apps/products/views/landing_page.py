from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def landing_page(request, product_id):
    product = Product.objects.filter(pk=product_id)
    if product.exists():
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/landing_page.html', {'product': product})
    return  redirect('all_products')