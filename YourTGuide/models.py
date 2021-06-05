from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    pass
# Create your models here.
class donar(models.Model):
    name=models.CharField(max_length=64)
    mobile=models.CharField(max_length=64)
    distr=models.CharField(max_length=64)
    group=models.CharField(max_length=64)
    diag=models.CharField(max_length=64)
class requests1(models.Model):
    name=models.CharField(max_length=64)
    mobile=models.CharField(max_length=64)
    distr=models.CharField(max_length=64)
    group=models.CharField(max_length=64)
class mobs(models.Model):
    num=models.CharField(max_length=100)
    usrr=models.CharField(max_length=64)
    def serialize(self):
        return {
            "num": self.num,
            
            
            "usrr": self.usrr
        }
    
