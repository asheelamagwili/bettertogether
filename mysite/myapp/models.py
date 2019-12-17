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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    #bio = models.TextField(max_length=500,blank=True)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #email = models.CharField(max_length=30)
    #username = models.CharField(max_length=30)
   
    def __str__(self):
        return self.user.username
    



