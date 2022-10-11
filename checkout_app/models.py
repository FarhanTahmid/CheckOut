from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(null=False,blank=False,primary_key=True,max_length=100)
    email_or_mobile=models.CharField(null=False,blank=False,max_length=50)
    
    def __str__(self):
        return self.username
