from django.urls import path,include

from . import views

app_name='public_user'
urlpatterns=[
    path('', views.login_page, name='login'),
    path('signup', views.signup_page, name="signup"),
    path('feed',views.user_feed,name='feed'),
]