# flake8: noqa
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-22 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_transfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('WIP', 'WIP'), ('Done', 'Done')], max_length=10)),
                ('memo', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.Account')),
            ],
        ),
    ]
