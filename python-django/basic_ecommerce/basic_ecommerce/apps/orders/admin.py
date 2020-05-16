from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'item_quantity', 'paid')


admin.site.register(Order, OrderAdmin)
