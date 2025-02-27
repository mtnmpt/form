from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import User

class A(admin.ModelAdmin):
    list_display = ['id','password','username','email','last_login','is_superuser','first_name','last_name','is_staff','is_active','date_joined','phone','address']

admin.site.register(MyUser,A)