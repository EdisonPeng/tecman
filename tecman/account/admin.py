from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('amount',)
    list_display = ('name', 'amount')
