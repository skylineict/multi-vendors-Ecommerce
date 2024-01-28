from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(max_length= 200)
    username = models.CharField(unique=True,max_length=20)
    bio  =   models.CharField(max_length =200)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.email
