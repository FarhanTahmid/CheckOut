from django.contrib import admin
from .models import signed_up_user
# Register your models here.
@admin.register(signed_up_user)
class Signed_up_User(admin.ModelAdmin):
    list_display=[
        'username',
        'email',
    ]