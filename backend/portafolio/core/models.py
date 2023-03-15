from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pro_img=models.ImageField()
    link_repo = models.CharField(max_length=100,default="")
    link_live = models.CharField(max_length=100,default="")

class About(models.Model):
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=1000)
    imagenabout = models.ImageField()
    
    
class Contact(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
