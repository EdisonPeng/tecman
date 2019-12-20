from django.db import models
from django.utils import timezone

from account.models import Account
from customer.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    shipping_fee = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)


class Platform(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    invoice_price = models.IntegerField(default=0)
    shipping_fee = models.IntegerField(default=0)
    tax = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    series_number = models.CharField(max_length=200, blank=True, default='')
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)

