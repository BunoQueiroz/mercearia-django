from django.shortcuts import render
from products.models import Product, Category

def all_products(request):
    products = Product.objects.filter(publicated=True)
    categorys = Category.objects.all()
    context = {
        'products': products,
        'categorys': categorys
    }
    return render(request, 'products/all_products.html', context)
