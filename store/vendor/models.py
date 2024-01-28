from django.db import models

# Create your models here.
from django.db import models
from shortuuid.django_fields  import ShortUUIDField
from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
from member.models import User

#this code record the vendors id and image upload files and save it that
def image_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
 


class Vendor(models.Model):
    vendor_id = ShortUUIDField(unique=True, length=8, prefix ='cat', max_length=20,alphabet='abcd2020')
    vendor_name= models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image =   models.ImageField(upload_to=image_directory_path, default='vendor.jpg')
    description = models.TextField(null=True, blank=True, default='i am a product seller')
    address =  models.CharField(max_length=300,default='Rivers State university')
    mobile =  models.CharField(max_length=300,default='+234890444')
    chat_response_time =  models.CharField(max_length=300,default='50')
    shiping_rating =  models.CharField(max_length=300,default='70')
    days_return =  models.CharField(max_length=300,default='46')
    warenty_period=  models.CharField(max_length=300,default='70')
    authentic_rating =  models.CharField(max_length=300,default='70')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.vendor_name
    
    def vendor_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />'% (self.image.url))
