# Generated by Django 4.1.4 on 2022-12-19 17:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_account_purchase_alter_purchase_hour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='purchase',
        ),
        migrations.AddField(
            model_name='purchase',
            name='account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='user.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='hour',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 12, 24, 695023)),
        ),
    ]