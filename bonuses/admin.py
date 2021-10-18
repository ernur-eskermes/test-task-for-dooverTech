from django.contrib import admin

from .models import Bonus


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'bonus',
        'valid_from',
        'valid_to',
        'active',
    )
