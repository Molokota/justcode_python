from django.contrib import admin
# from django.contrib.auth.models import 
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'nickname',
        'mobile_phone',
        'date_joined',
        'position',
    ]
