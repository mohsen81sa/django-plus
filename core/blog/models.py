from django.db import models
from accounts.models import *
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title 

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name    