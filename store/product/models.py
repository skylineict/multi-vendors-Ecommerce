from django.db import models
from shortuuid.django_fields  import ShortUUIDField
from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
from member.models import User
from vendor.models import Vendor
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

def image_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Category(models.Model):
    categoryid = ShortUUIDField(unique=True, length=8, prefix ='cat', max_length=20,alphabet='abcd2020')
    category_name = models.CharField(max_length=200)
    image =   models.ImageField(upload_to='category', default='category.jpg')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
    def category_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />'% (self.image.url))


Order_Status = (
('process', 'Processing'),
('shipped',   'Shipped'),
('dilivered',  'Delivered')

)




Status = (
('draft', 'Draft'),
('disable',   'Disable'),
('reject',  'Reject'),
('in review',  'In Review'),
('approved',  'Approved')

)


Rating = [
        (1, '⭐☆☆☆☆'),
        (2, '⭐⭐☆☆☆'),
        (3, '⭐⭐⭐☆☆'),
        (4, '⭐⭐⭐⭐☆'),
        (5, '⭐⭐⭐⭐⭐')
    ]



class Products(models.Model):
    product_id = ShortUUIDField(unique=True, length=8, prefix ='pro', max_length=20,alphabet='abcd2020')
    product_name= models.CharField(max_length=200)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    vendors= models.ForeignKey(Vendor,  on_delete=models.CASCADE, null=True, related_name='products')
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True, related_name='product')
    image =   models.ImageField(upload_to=image_directory_path, default='product.jpg')
    description = RichTextUploadingField(null=True, blank=True)
    sommary_product_info= RichTextUploadingField(null=True, blank=True )
    # description = models.TextField(null=True, blank=True, default='elibook laptop')
    price =   models.DecimalField(max_digits=60,decimal_places=2,default=70)
    old_price =   models.DecimalField(max_digits=60,decimal_places=2,default=90.93)
    # spefications = models.TextField(null=True, blank=True)
    spefications = RichTextUploadingField(null=True, blank=True)
    product_status  = models.CharField(choices=Status, max_length=200, default='in review')
    status =   models.BooleanField(default=True)
    in_stock =   models.BooleanField(default=True)
    features =   models.BooleanField(default=False)
    digital =   models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, length=4, prefix ='pro', max_length=10,alphabet='1234578')
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(null=True, blank=True)
    productkind = models.CharField(max_length=200, null=True, blank=True, default='best selling')
    my_stock = models.CharField(max_length=200, null=True, blank=True, default='10')
    expiration = models.CharField(max_length=200, null=True, blank=True, default='200 days')
   

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
    
    def product_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />'% (self.image.url))
    
    def get_product_precentage(self):
        if self.old_price:
            new_price = (self.price- self.old_price) / abs(self.old_price) * 100
        return new_price
    

    
class Productimage(models.Model):
    product_names = models.ForeignKey(Products,  on_delete=models.CASCADE, null=True,related_name='product_images')
    images =   models.ImageField(upload_to='product-images', default='product.jpg')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products images'

    def __str__(self):
        return self.product_names.product_name
    


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    paid_status =   models.BooleanField(default=False)
    price =   models.DecimalField(max_digits=60,decimal_places=2,default=70.90)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status  = models.CharField(choices=Order_Status, max_length=200, default='process')


    class Meta:
        verbose_name_plural = 'Cart Orders'

    def __str__(self):
        return self.product


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder,  on_delete=models.CASCADE, null=True)
    product_satus= models.CharField(max_length=200)
    item= models.CharField(max_length=200)
    image= models.CharField(max_length=200)
    price =   models.DecimalField(max_digits=60,decimal_places=2,default=70.90)
    total =   models.DecimalField(max_digits=60,decimal_places=2,default=70.90)
    qty = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Cart Orders'

    def __str__(self):
        return self.product
    
    def cartitem_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />'% (self.image.url))

RATING_CHOICES = [
        (1, '⭐☆☆☆☆'),
        (2, '⭐⭐☆☆☆'),
        (3, '⭐⭐⭐☆☆'),
        (4, '⭐⭐⭐⭐☆'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE, null=True)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)



    def __str__(self):
        return self.review


    

    def get_rating(self):
        return self.rating
    
    class Meta:
        verbose_name_plural = 'Product Reviews'
    
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


    

    def __str__(self):
        return self.product
    



class orderaddress(models.Model):
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Status =  models.BooleanField(False)






