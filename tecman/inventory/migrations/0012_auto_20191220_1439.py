# Generated by Django 3.0 on 2019-12-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20191220_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='tax',
            field=models.IntegerField(default=0),
        ),
    ]
