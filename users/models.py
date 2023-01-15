from django.db import models

class Registered_Users(models.Model):
    username=models.CharField(null=False,blank=False,primary_key=True,max_length=100)
    email=models.EmailField(null=False,blank=False)

    class Meta:
        verbose_name="Registered User"
    def __str__(self) -> str:
        return self.username