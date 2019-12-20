# Generated by Django 3.0 on 2019-12-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20191217_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='avg_price',
        ),
        migrations.AddField(
            model_name='shipment',
            name='series_number',
            field=models.CharField(default=12345, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='delivery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.DeliveryMethod'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Platform'),
        ),
    ]