# Generated by Django 3.0 on 2019-12-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20191214_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='shipping_fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='tax',
            field=models.IntegerField(),
        ),
    ]
