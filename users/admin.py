from django.contrib import admin
from . models import Registered_Users
# Register your models here.
@admin.register(Registered_Users)
class Registered_User(admin.ModelAdmin):
    list_display=[
        'username','email'
    ]