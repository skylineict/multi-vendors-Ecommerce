# Generated by Django 4.2.9 on 2024-02-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='invoice_No',
            field=models.CharField(default='No2304', max_length=200),
        ),
    ]
