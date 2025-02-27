from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    phone = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)