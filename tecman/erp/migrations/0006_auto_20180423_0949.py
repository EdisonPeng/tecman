# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20180423_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatingexpense',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='operating_expense', to='erp.Account'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='dst_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_dst', to='erp.Account'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='src_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_src', to='erp.Account'),
        ),
    ]