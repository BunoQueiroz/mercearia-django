# Generated by Django 4.1.4 on 2022-12-13 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 14, 52, 17, 414643)),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]