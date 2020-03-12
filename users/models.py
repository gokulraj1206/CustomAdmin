from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, AbstractUser
)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

def __str__(self):
        return self.username

#USERNAME_REGEX = ''
'''
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    USERNAME_FIELD = 'username'
    # add additional fields in here
    

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property   
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

'''