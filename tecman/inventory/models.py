from django.db import models
from django.utils import timezone

from account.models import Account
from customer.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    avg_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    shipping_fee = models.IntegerField()
    tax = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)


class Shipment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    shipping_fee = models.IntegerField()
    tax = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)

