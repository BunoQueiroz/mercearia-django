from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'publicated', 'category')
    list_editable = ('price', 'publicated')
    list_display_links = ('category',)
    list_per_page = 10
    list_filter = ('name', 'category')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
