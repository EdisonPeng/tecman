# Generated by Django 3.0 on 2019-12-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20191220_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='tax',
            field=models.IntegerField(),
        ),
    ]
