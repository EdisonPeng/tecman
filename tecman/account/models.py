from django.db import models
from django.utils import timezone


class Account(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    src_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='src_account')
    dst_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='dst_account')
    amount = models.IntegerField()
    exchange_rate = models.FloatField(default=1.0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'transfer %s from %s to %s' % (self.amount, self.src_account, self.dst_account)
