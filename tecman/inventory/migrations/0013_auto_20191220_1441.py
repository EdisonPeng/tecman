# Generated by Django 3.0 on 2019-12-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20191220_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='series_number',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]