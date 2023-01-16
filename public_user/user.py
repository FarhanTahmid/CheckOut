from . models import signed_up_user
from django.contrib.auth.models import User,auth

class Public_Users:
    
    def login(request):
        username=input("Enter the username: ")
        password=input("Enter your password")
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            print("logged in")
        else:
            print("cant login")
        
    def signup(request,username,email,password,confirm_password):
        
        if password==confirm_password:
            try:
                signed_up_user.objects.get(username=username)
                print("username already exists")
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
                print("user created")
                auth.login(request,user)
                print("Logged in")