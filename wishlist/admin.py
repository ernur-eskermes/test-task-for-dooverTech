from django.contrib import admin

from .models import WishlistItem, Wishlist


class WishlistItemInline(admin.StackedInline):
    model = WishlistItem


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'client',
    )
    inlines = [WishlistItemInline]
