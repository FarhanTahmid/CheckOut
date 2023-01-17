from django.shortcuts import render,redirect
from . user import Public_Users
# Create your views here.
def login_signup_page(request):
    #login
    # username=input("Enter username: ")
    # password=input("Enter Password: ")
    
    # if(Public_Users.login(request,username,password)):
    #     return redirect('public_user:feed')
    # else:
    return render(request, "login_signup_page.html")
    
    

def user_feed(request):
    return render(request,"user_feed.html")