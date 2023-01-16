from django.shortcuts import render
from . user import Public_Users
# Create your views here.
def login_signup_page(request):
    #signup
    username=input("Enter username: ")
    email=input("Enter email: ")
    password=input("Enter Password: ")
    confirm_password=input("Confirm Password: ")
    Public_Users.signup(request,username,email,password,confirm_password)
    
    return render(request, "login_signup_page.html")