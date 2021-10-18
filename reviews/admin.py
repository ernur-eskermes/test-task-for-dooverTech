from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'rate',
        'subject',
        'product',
        'status',
    )
    raw_id_fields = (
        'product',
        'client',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'subject',
        'product'
    )
