# Generated by Django 4.2.9 on 2024-01-28 08:03

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_status', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=70.9, max_digits=60)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('product_status', models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('dilivered', 'Delivered')], default='process', max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart Orders',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryid', shortuuid.django_fields.ShortUUIDField(alphabet='abcd2020', length=8, max_length=20, prefix='cat', unique=True)),
                ('category_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='category.jpg', upload_to='category')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcd2020', length=8, max_length=20, prefix='pro', unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('image', models.ImageField(default='product.jpg', upload_to=product.models.image_directory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('sommary_product_info', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=70, max_digits=60)),
                ('old_price', models.DecimalField(decimal_places=2, default=90.93, max_digits=60)),
                ('spefications', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('draft', 'Draft'), ('disable', 'Disable'), ('reject', 'Reject'), ('in review', 'In Review'), ('approved', 'Approved')], default='in review', max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('features', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234578', length=4, max_length=10, prefix='pro', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('productkind', models.CharField(blank=True, default='best selling', max_length=200, null=True)),
                ('my_stock', models.CharField(blank=True, default='10', max_length=200, null=True)),
                ('expiration', models.CharField(blank=True, default='200 days', max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(choices=[(1, '⭐☆☆☆☆'), (2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆'), (4, '⭐⭐⭐⭐☆'), (5, '⭐⭐⭐⭐⭐')], default=1)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.products')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='Productimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_names', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.products')),
            ],
            options={
                'verbose_name_plural': 'Products images',
            },
        ),
        migrations.CreateModel(
            name='orderaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('Status', models.BooleanField(verbose_name=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_satus', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=70.9, max_digits=60)),
                ('total', models.DecimalField(decimal_places=2, default=70.9, max_digits=60)),
                ('qty', models.IntegerField(default=0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.cartorder')),
            ],
            options={
                'verbose_name_plural': 'Cart Orders',
            },
        ),
    ]
