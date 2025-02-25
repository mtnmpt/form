from django.urls import path
from .views import *
urlpatterns = [
    path(route='login',view=login,name='login')
]
