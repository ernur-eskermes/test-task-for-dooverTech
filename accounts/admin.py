from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'bonus'
    )
    search_fields = (
        'user__username',
        'user__phone',
        'user__first_name',
        'user__last_name',
    )
