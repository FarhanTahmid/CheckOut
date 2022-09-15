from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    """The home page for checkout"""
    return render(request, 'homepage.html')
