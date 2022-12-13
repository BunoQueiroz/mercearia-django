from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'publicated', 'category')
    list_editable = ('price',)
    list_display_links = ('category',)
    list_per_page = 10
    list_filter = ('name', 'category')

admin.site.register(Product,ProductAdmin)
