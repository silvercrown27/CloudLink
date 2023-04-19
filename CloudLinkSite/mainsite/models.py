from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, blank=False, unique=True)
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, blank=False)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    zip = models.IntegerField()
    password = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.username

class MyMedia(models.Model):
    image = models.ImageField(upload_to='media/')