from doctest import FAIL_FAST
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,username,**extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")
        user=self.model(
            email=self.normalize_email(email),
            username=username
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,password,username,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,username,password,**extra_fields)
    
    def create_superuser(self,email,password,username,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,username,**extra_fields)

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email_or_mobile=models.CharField(unique=True,max_length=254)
    username=models.CharField(max_length=100)
    
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    
    objects=CustomUserManager()
    USERNAME_FIELD='email_or_mobile'
    REQUIRED_FIELDS= ['username']
    class Meta:
         verbose_name='User'
         verbose_name_plural='Users'