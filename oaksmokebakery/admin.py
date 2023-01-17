from django.contrib import admin
from .models import Item, OrderCart, OrderItem


admin.site.register(Item)
admin.site.register(OrderCart)
admin.site.register(OrderItem)

class OrderItemAdmin(admin.ModelAdmin):
    """ An admin panel for viewing macrame objects """
    list_display = (
        'item',
        'price',
    )

    ordering = ('-item',)
