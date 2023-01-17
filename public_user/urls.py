from django.urls import path,include

from . import views

app_name='public_user'
urlpatterns=[
    path('', views.login_signup_page, name='login_signup_page'),
    
    path('feed',views.user_feed,name='feed'),
]