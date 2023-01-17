from django.db import models

# Create your models here.
class signed_up_user(models.Model):
    username=models.CharField(null=False,blank=True,primary_key=True,max_length=50)
    email=models.EmailField(null=False,blank=False)
    
    class Meta:
        verbose_name="Signed in Users in Checkout Site"

        def __str__(self) -> str:
            return self.username