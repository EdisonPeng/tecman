# Generated by Django 3.0 on 2019-12-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20191220_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='invoice_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='tax',
            field=models.IntegerField(),
        ),
    ]
