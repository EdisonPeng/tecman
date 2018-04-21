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
    src_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='src_account')
    dst_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='dst_account')
    amount = models.IntegerField()
    memo = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
