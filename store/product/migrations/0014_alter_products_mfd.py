# Generated by Django 5.0.1 on 2024-01-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_rename_exp_products_expiration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='mfd',
            field=models.DateTimeField(blank=True, default='2007-03-22 04:30', null=True),
        ),
    ]