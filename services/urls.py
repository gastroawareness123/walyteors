from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:id>', doctor_service_page_view, name='doctor_service_page'),
    path('select-language/', language_selected_page_view, name='language_selected_page'),
    path('', index_page, name='index')    
]