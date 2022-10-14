from distutils import errors
from distutils.command.config import config
from django.db import DatabaseError
from django.shortcuts import render,redirect
import pyrebase
from checkout_app.user.signup import CommonUser
from checkout_app.user.generate import Generators
from django.contrib import messages

config={
    "apiKey": "AIzaSyCs-CW9vsD3jWGQOfyDznnvo5bg60g0gHo",
    "authDomain": "checkouttest-c5528.firebaseapp.com",
    "databaseURL": "https://checkouttest-c5528-default-rtdb.firebaseio.com",
    "projectId": "checkouttest-c5528",
    "storageBucket": "checkouttest-c5528.appspot.com",
    "messagingSenderId": "686410994548",
    "appId": "1:686410994548:web:33493b9b0ce36cee2b9221",
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
database=firebase.database()


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
        elif(CommonUser.userSignup(email_or_mobile=emailOrMobile,password=password)=='u'):
            signUp(request)
            return redirect('checkout_app:signup')
        else:
            print("You are in homepage now")
            return redirect('checkout_app:signup')
    else:
        return render(request,'signup.html')

def login(request):
    '''Goes to login form from signup page upon signup true. accessible from index'''
    return render(request,'login.html')
