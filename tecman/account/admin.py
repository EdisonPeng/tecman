from django.contrib import admin

from .models import Account, Transfer


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('src_account', 'dst_account', 'amount', 'exchange_rate', 'date')
