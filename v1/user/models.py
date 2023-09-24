from django.db import models
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from v1.bank.models import Bank

# Create your models here.
class User(AbstractUser):
    GenderChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Don\'t Specify'),
    ]
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.EmailField(verbose_name='email', unique=True, max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.CharField(max_length=101, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    reputation = models.IntegerField(default=100)
    facebook_username = models.CharField(blank=True, null=True, max_length=255)
    linkedin_username = models.CharField(blank=True, null=True, max_length=255)
    twitter_username = models.CharField(blank=True, null=True, max_length=255)
    is_email_verified = models.BooleanField(default=False)
    profile_pic = models.ImageField(default='user/egg.jpg', upload_to='user/')
    gender = models.CharField(
        max_length=2,
        choices=GenderChoices,
        null=True
    )
    REQUIRED_FIELDS = ['username','first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


def generate_username(instance):
    first_name = slugify(instance.first_name)
    last_name = slugify(instance.last_name)
    val = "{0}.{1}".format(first_name,last_name).lower()
    x=0
    while True:
        if x == 0 and User.objects.filter(username=val).count() == 0:
            return val
        else:
            new_val = "{0}{1}".format(val,x)
            if User.objects.filter(username=new_val).count() == 0:
                return new_val
        x += 1
        if x > 1000000:
            raise Exception("Name is super popular!")

def pre_save_post_receiver(sender, instance, *args,**kwargs):
    if not instance.username:
        instance.username= generate_username(instance)

pre_save.connect(pre_save_post_receiver, sender=User)