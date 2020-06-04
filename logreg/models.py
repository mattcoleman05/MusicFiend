from django.db import  models
from django.db.models import Model
import re

class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        # confirmations = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = ("The email address you've entered is the incorrect format")
        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2:
            errors['lname'] = "Last Name must be more than 2 characters."
            errors['fname'] = "First name must be more than 2 characters."
        if postdata['password'] != postdata['confirmpassword']:
            errors['password'] = 'Password and Confirm Password do not match'
        return errors



        




class User(models.Model):
    artistname = models.CharField(max_length = 50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    

class ArtistInfo(models.Model):
    genre = models.CharField(max_length = 25)
    profile = models.CharField(max_length = 500)
    members = models.CharField(max_length= 50)
    city = models.CharField(max_length = 50)
    link = models.URLField(max_length = 100)
    record_label = models.CharField(max_length = 50)
    user = models.ForeignKey(User, related_name= 'info', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist_image = models.ImageField(upload_to='images/', blank = True)

    def __str__(self):
        return self.user


class AlbumInfo(models.Model):
    members = models.TextField()
    label = models.CharField(max_length = 50)
    title = models.CharField(max_length = 75)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name = 'albuminfo', on_delete=models.CASCADE)

    



class ArtistImage(models.Model): 
    artist_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title




