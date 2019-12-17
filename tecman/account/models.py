from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name