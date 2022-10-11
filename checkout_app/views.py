from distutils.command.config import config
from django.db import DatabaseError
from django.shortcuts import render,redirect
import pyrebase

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
    '''Goes to signup form from index page'''
    emailOrMobile=''
    password=''
    if(request.method=="POST"):
        emailOrMobile=request.POST['mobile_or_email']
        password=request.POST['password']
    print(emailOrMobile)
    print(password)
    
    
    
    
    print(f"Website name is {database.child('Data').child('Name').get().val()}")
    return render(request,'signup.html')
def login(request):
    '''Goes to login form from signup page upon signup true. accessible from index'''
    return render(request,'login.html')
