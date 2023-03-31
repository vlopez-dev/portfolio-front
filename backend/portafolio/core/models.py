from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms.widgets import Textarea

# Create your models here.




class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    pro_img=models.ImageField()
    link_repo = models.CharField(max_length=100,default="")
    link_live = models.CharField(max_length=100,default="")


    def __str__(self):
                return self.name



class Technology(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    project=models.ManyToManyField('Project',related_name='technologys')




    def __str__(self):
            return self.name






class About(models.Model):
    title = models.CharField(max_length=50)
    description= models.TextField(max_length=1000)
    imagenabout = models.ImageField()



    def __str__(self):
            return self.title

class Contact(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)





    def __str__(self):
            return self.title
class Certificate(models.Model):
    title = models.CharField(max_length=50)
    imagecert = models.ImageField()




    def __str__(self):
            return self.title