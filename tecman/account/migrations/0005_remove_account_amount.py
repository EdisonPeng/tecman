# Generated by Django 3.0 on 2019-12-20 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191217_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='amount',
        ),
    ]
