from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#this aids in generation of SQL code

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    image=models.ImageField()
    image_title=models.TextField(default="No image description title available")
    image_alt_text=models.TextField(default="No image alt text available") 


    def __str__(self): 
        return self.title

class Contact(models.Model):
    address=models.TextField()
    contact_number=models.TextField()
    email=models.EmailField()
    addr_link=models.URLField(default="#")

class About(models.Model):
    about=models.TextField()
    other_links=models.URLField(default="#")

class Product(models.Model):
    name=models.TextField()
    description=models.TextField()
    available=models.TextField()
    image=models.ImageField()