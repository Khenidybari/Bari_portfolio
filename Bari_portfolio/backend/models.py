from django.db import models

from django.contrib.auth.models import AbstractUser 
class User(AbstractUser):
    email = models.CharField(max_length=200, null = True, blank=True)
    password = models.CharField(max_length = 250, null = True, blank = True)
    profile_pic = models.FileField(upload_to='images/', null = True, blank = True)
    about_me = models.CharField(max_length = 250, null = True, blank = True)
    address = models.CharField(max_length = 250, null = True, blank = True)
    contact = models.CharField(max_length = 250, null = True, blank = True)
    facebook = models.CharField(max_length = 250, null = True, blank = True)
    instagram = models.CharField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.email
    
class Skill(models.Model):
    title = models.CharField(max_length=200, null = True, blank=True)
    description = models.CharField(max_length=200, null = True, blank=True)
    icon = models.FileField(upload_to='images/', null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    image = models.FileField(upload_to='images/', null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

