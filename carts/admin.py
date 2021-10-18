from django.contrib import admin

from carts.models import Cart, CartItem


class CartItemInline(admin.StackedInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'total',
    )
    inlines = [CartItemInline]
