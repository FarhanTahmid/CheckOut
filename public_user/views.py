from django.shortcuts import render,redirect
from . user import Public_Users
from django.contrib import messages
# Create your views here.

def login_page(request):
    #Django user Login
    if(request.method=="POST"):
        #checking if the login button was pressed
        if(request.POST.get('login')):
            #getting all the credentials
            username=request.POST['username']
            password=request.POST['password']
            
            #checking the returned values from login method in Public Users
            
            if(Public_Users.login(request,username,password)):
                return redirect('public_user:feed')
            else:
                messages.info(request,"Credentials given are wrong! Try again")
        #checking if the facebook login button was clicked
        if(request.POST.get('facebook_login')):
            return redirect('social:begin', 'facebook')   
            
    return render(request, "Login.html")

def signup_page(request):
    ##Django user signup##
    #checking if the method is post
    if(request.method=="POST"):
        #checking if the signup button was clicked
        if(request.POST.get("signup")):
            #getting signup credentials. Not using one liner
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            

            #checking if a password mismatch occured
            if(Public_Users.signup(request,username,email,password,confirm_password))=="pass_mismatch":
                messages.info(request,"Two Passwords did not match! Please try Again")
            
            elif(Public_Users.signup(request,username,email,password,confirm_password))==False:
                messages.info(request,"There is already a User registered with this username in our database. Please try with another username")
                    
            #checking if the returned value is True from signup method of Public_Users class
            elif(Public_Users.signup(request,username,email,password,confirm_password))==True:
                #showing signup success message (not important)
                messages.info(request,"Signup Successful")
                #Login the user for the first time directly with the password
                if(Public_Users.login(request,username,password)):
                    return redirect('public_user:feed')
                else:
                    messages.info(request,"Could not log you in directly. Please go to the Login option and enter your credentials to login!")
        
            
            
          
            
    return render(request, "signup.html")   
    

def user_feed(request):
    return render(request,"user_feed.html")