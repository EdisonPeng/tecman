from django.contrib import admin

from .models import Product, Purchase, Shipment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('amount', 'avg_price')
    list_display = ('name', 'amount', 'avg_price')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'price', 'shipping_fee', 'tax', 'account', 'date')
    date_hierarchy = 'date'

    def _get_avg_price(self, avg_price, stock, added_price, added_amount):
        ori_price = avg_price * stock
        new_avg_price = (ori_price + added_price)/(stock + added_amount)
        return new_avg_price

    def save_model(self, request, obj, form, change):
        obj.product.avg_price = self._get_avg_price(
                obj.product.avg_price,
                obj.product.amount,
                obj.price,
                obj.amount)
        obj.product.amount += obj.amount
        obj.product.save()
        obj.account.amount -= obj.price
        obj.account.save()
        super().save_model(request, obj, form, change)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'price', 'account', 'date')
    date_hierarchy = 'date'

    def save_model(self, request, obj, form, change):
        obj.product.amount -= obj.amount
        obj.product.save()
        obj.account.amount += obj.price
        obj.account.save()
        super().save_model(request, obj, form, change)