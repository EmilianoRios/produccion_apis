from django.urls import path
from . import views

urlpatterns = [
    path('', views.DigimonApi , name="index"),
    path('search/',views.searchDigimonAPi, name="search")
]