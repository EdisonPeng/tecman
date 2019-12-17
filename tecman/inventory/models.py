from django.db import models
from django.utils import timezone

from account.models import Account
from customer.models import Customer


platforms = [
        ('shoppe', 'shoppe'),
        ('pcone', 'pcone'),
        ('group_buy', 'group_buy')
]
delivery_methods = [
        ('ktj', 'ktj'),
        ('post', 'post'),
]

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
    shipping_fee = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)


class Shipment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    shipping_fee = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    platform = models.CharField(max_length=10, choices=platforms, default='shoppe')
    delivery_method = models.CharField(max_length=10, choices=delivery_methods, default='ktj')
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return '%s * %s = %s' % (self.product, self.amount, self.price)

