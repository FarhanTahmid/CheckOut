"""Defines URL patterns for checkout_app"""

from django.urls import path

from . import views

app_name= 'checkout_app'
urlpatterns=[
    # Home page
    path('', views.homepage, name='homepage'),
]