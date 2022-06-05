from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register-doctor-hit/', doctor_hits_api, name='doctor-hits-api'),
    path('get-images/', get_images)
]