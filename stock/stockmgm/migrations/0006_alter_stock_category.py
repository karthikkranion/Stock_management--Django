# Generated by Django 5.1.4 on 2025-01-19 12:32

import stockmgm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgm', '0005_remove_stock_datefield_alter_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(max_length=55, verbose_name=stockmgm.models.Category),
        ),
    ]
