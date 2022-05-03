from django.urls import path
from menuApis import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    path('',views.menuApis,name="Home"),
]