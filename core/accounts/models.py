from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_field):
        '''
        create and save a user with the given email and password and extra data
        '''
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_field):
        '''
        create and save a superuser with the given email and password and extra data
        '''
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_Staff=True"))
        if extra_field.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_Superuser=True"))
        
        return self.create_user(email, password, **extra_field)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_Date = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self) -> str:
        return self.email