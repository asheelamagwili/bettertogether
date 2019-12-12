from django.db import models
from django.contrib.auth.models import User

# White board
class WhiteBoard(models.Model):
    subject = models.CharField(max_length=30)
    user = models.ManyToManyField(User)
    whiteboard_key = models.IntegerField()

    def __str__(self):
        return self.subject

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    bio = models.CharField(max_length=500,blank=True)
