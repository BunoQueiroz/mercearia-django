# Generated by Django 4.1.4 on 2022-12-18 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_date_create_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 11, 41, 8, 727263)),
        ),
    ]
