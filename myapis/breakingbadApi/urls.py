from unicodedata import name
from django.contrib import admin
from django.urls import path
from breakingbadApi import views

urlpatterns = [
    path("", views.home, name="home_breakingbad" ),
    path("episodios/", views.episodios, name="episodios"),
]