from django.contrib import admin

from .models import Product, Purchase, Shipment, Platform, DeliveryMethod


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'price', 'shipping_fee', 'tax', 'account', 'date')
    date_hierarchy = 'date'


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'price', 'invoice_price', 'shipping_fee', 'tax', 'customer', 'platform', 'delivery_method', 'series_number', 'account', 'date')
    exclude = ('tax',)
    autocomplete_fields = ["customer"]
    date_hierarchy = 'date'

    def save_model(self, request, obj, form, change):
        obj.tax = obj.invoice_price / 21
        super().save_model(request, obj, form, change)
