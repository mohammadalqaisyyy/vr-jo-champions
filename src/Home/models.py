from distutils.command.upload import upload
from tkinter import PhotoImage
from turtle import title
from django.db import models

# Create your models here.
class home(models.Model):
    homeText = models.CharField(max_length=100)
    DesText = models.TextField(default='')
    homeImage = models.ImageField(upload_to='home_img/')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "home_" + str(self.id)

class Challenges(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(default='')
    photo=models.ImageField(upload_to='Challenges_img/')
    date= models.DateTimeField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class about_us(models.Model):
    text=models.TextField(default='')
    bottunText =models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "about_" + str(self.id)

class our_goal(models.Model):
    text=models.TextField(default='')
    bottunText =models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "about_" + str(self.id)

class contact(models.Model):
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=254)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "contact_" + str(self.id)

class training(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(default='')
    photo=models.ImageField(upload_to='Training_img/')
    date= models.DateTimeField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

