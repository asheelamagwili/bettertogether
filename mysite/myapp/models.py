from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver

from django.db.models.signals import post_save



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


#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = Profile.objects.create(user=kwargs['instance']) 

#post_save.connect(create_profile, sender=User) 
# 
# 
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()


    def __str__(self):
        return self.first_name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



