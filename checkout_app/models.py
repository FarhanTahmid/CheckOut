from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(null=False,blank=False,primary_key=True,max_length=100)
    