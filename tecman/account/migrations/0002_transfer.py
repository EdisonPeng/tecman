# Generated by Django 3.0 on 2019-12-17 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('dst_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dst_account', to='account.Account')),
                ('src_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_account', to='account.Account')),
            ],
        ),
    ]
