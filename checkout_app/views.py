from distutils import errors
from distutils.command.config import config
from operator import imod
from django.db import DatabaseError
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
import pyrebase
from checkout_app.user.signup import CommonUser
from checkout_app.user.generate import Generators
from django.contrib import messages



# Create your views here.
def homepage(request):
    """The home page for checkout"""
    return render(request, 'index.html')
def signUp(request):
    '''Goes to signup from index page'''
    emailOrMobile=''
    password=''
    if(request.method=="POST"):
        emailOrMobile=request.POST['mobile_or_email']
        password=request.POST['password']
        if(CommonUser.userSignup(email_or_mobile=emailOrMobile,password=password)==False):
            messages.info(request,"This email is already in use with another account")
            return redirect('checkout_app:signup')
        else:
            print("You are in homepage now")
            return redirect('checkout_app:signup')
    else:
        return render(request,'signup.html')

def logIn(request):
    '''Goes to login form from signup page upon signup true. accessible from index'''
    if request.method=='POST':
        username=request.POST['email_or_mobile']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            print("You are in homepage now")
            return redirect('checkout_app:logIn')
            #return redirect('users:menu')
        else:
            messages.info(request,'Credentials given are wrong')
            print('Credentials given are wrong')
            return redirect('checkout_app:logIn')
    else:
        return render(request,'login.html')