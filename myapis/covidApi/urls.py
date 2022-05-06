from django.urls import path
from .views import listaPais


urlpatterns = [
    path('', listaPais, name='InicioCovid'),

]
