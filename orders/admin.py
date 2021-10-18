from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'shipping_address',
        'order_total',
        'braintree_id',
    )
