from django.contrib import admin

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent'
    )
    raw_id_fields = (
        'parent',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'quantity',
        'price',
    )
    raw_id_fields = (
        'category',
    )
    search_fields = (
        'name',
    )
