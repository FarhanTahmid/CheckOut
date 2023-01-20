from . models import signed_up_user
from django.contrib.auth.models import User,auth

class Public_Users:
    
    def login(request,username,password):
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return True
        else:
            return False
        
    def signup(request,username,email,password,confirm_password):
        
        if(password==confirm_password):
            try:
                signed_up_user.objects.get(username=username)
                return False
            except signed_up_user.DoesNotExist:
                #for checkout database
                new_user=signed_up_user(
                    username=username,
                    email=email
                )
                new_user.save()
                #for django signnup
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                #return true if user is created
                return True
        else:
            return "pass_mismatch"