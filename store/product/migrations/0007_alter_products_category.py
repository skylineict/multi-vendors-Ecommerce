# Generated by Django 5.0.1 on 2024-01-23 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category'),
        ),
    ]