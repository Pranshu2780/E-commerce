from django.db import models
from django.contrib.auth.models import user
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE,null=True,blank=True);
    name = models.CharField(max_length=200, null=True);
    email = models.CharField(max_length=200, null=True);

    def __str__(self):
        return self.name

class Product():
        