from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email= models.EmailField(null=True,unique=True)
    phone_number= models.CharField(max_length=30,null=True)
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contract_number = models.IntegerField(default=0,null=True)
    date_time = models.DateTimeField(default=datetime.now,)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []