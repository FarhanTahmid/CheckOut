from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    """The home page for checkout"""
    return render(request, 'index.html')
def signUp(request):
    '''Goes to signup form from index page'''
    return render(request,'signUpForm.html')
def login(request):
    '''Goes to login form from signup page upon signup true. accessible from index'''
    return render(request,'loginPage.html')
