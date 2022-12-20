from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'is_superuser')
    list_editable = ('is_superuser', )
    list_per_page = 10

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('account', 'items', 'amount', 'hour')
    list_display_links = ('items',)
    list_per_page = 10
    list_filter = ('account',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Account)
