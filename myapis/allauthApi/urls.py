from django.urls import path
from allauthApi import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',LoginView.as_view(template_name='allauthApi/login.html'),name='LogIn'),
    path('logout/',LogoutView.as_view(template_name='allauthApi/logout.html'),name='LogOut'),
    path('register/',views.register,name='Register'),
]