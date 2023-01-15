from django.urls import path

from . import views

app_name= 'checkout_site'
urlpatterns=[
    # Home page
    path('', views.homepage, name='homepage'),
       
]