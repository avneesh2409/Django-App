from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=True)
    portfolio = models.URLField(blank = True)
    # image = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username
