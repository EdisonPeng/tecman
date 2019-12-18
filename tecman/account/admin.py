from django.contrib import admin

from .models import Account, Transfer


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('amount',)
    list_display = ('name', 'amount')


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('src_account', 'dst_account', 'amount', 'exchange_rate', 'date')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['src_account', 'dst_account', 'amount', 'exchange_rate']
        else:
            return []

    def save_model(self, request, obj, form, change):
        obj.src_account.amount -= obj.amount
        obj.src_account.save()
        obj.dst_account.amount += (obj.amount / obj.exchange_rate)
        obj.dst_account.save()
        super().save_model(request, obj, form, change)
