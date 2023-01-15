from django.shortcuts import render
from users.models import Registered_Users
# Create your views here.
def login(request):
    if(request.method=="POST"):
        if(request.POST.get('login_button')):

            username=request.POST['email_or_mobile'] 
            password=request.POST['password']
            print(f"Username: {username}")
            print(f"Password: {password}")
        if(request.POST.get('facebook_login')):
            print("facebook button")
        if(request.POST.get('google_login')):
            print('google login')
   
    return render(request, 'login.html')
def signup(request):
    if(request.method=="POST"):
        if(request.POST.get('signup_button')):
            
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if(password==confirm_password):
                user=Registered_Users(
                    username,email
                )
                user.save()

        if(request.POST.get('facebook_signup_button')):
            print("facebook button")  
        if(request.POST.get('google_signup_button')):
            print("google button")    
    return render(request, 'signup.html')