# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=30)
    balance = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    src_account = models.ForeignKey(Account, on_delete=models.PROTECT,
                                    related_name='transfer_src')
    dst_account = models.ForeignKey(Account, on_delete=models.PROTECT,
                                    related_name='transfer_dst')
    amount = models.IntegerField()
    memo = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)


class OperatingExpense(models.Model):
    STATUS = (
        ('WIP', 'WIP'),
        ('Done', 'Done'),
    )
    item = models.CharField(max_length=100)
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT,
                                related_name='operating_expense')
    status = models.CharField(max_length=10, choices=STATUS)
    memo = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
