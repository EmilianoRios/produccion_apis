from unicodedata import name
from django.contrib import admin
from django.urls import path
from disneyApi import views

urlpatterns = [
    path("", views.home, name="home_disney"),
    
]