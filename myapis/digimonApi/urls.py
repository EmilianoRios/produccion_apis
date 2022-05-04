from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DigimonApi , name="index"),
    path('search/',views.searchDigimonAPi, name="search")
]