from django.shortcuts import render

# Create your views here.
def login_signup_page(request):
    return render(request, "login_signup_page.html")