# Generated by Django 5.0.1 on 2024-01-25 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_products_mfd_alter_products_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='expiration',
        ),
        migrations.RemoveField(
            model_name='products',
            name='mfd',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='products',
            name='type',
        ),
    ]