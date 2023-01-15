from django.contrib import admin
from .models import Item, OrderCart, OrderItem


admin.site.register(Item)
admin.site.register(OrderCart)
admin.site.register(OrderItem)
