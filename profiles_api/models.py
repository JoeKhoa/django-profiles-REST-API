        # https://docs.djangoproject.com/en/1.10/topics/db/managers/#custom-managers-and-model-inheritance

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password = None):
        """ Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)
        # print('test')
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create and use new user with the given detail"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """docstring for UseProfile."""
    email = models.EmailField(max_length = 255, unique=True )
    name = models.CharField(max_length=255)
    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects  = UserProfileManager()    # used in future

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        """ Retrieve fullname of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short-name of user"""
        return self.name
