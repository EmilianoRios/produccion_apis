from django.contrib import admin
from django.urls import path,include

""" 
PARA INCLUIR LAS URLS DE TU APP SE UTILIZA

path('nombreApi/',include('nombreApi.urls'))

RECORDAR INCLUIR LAS COMILLAS DENTRO DE LA FUNCIÓN INCLUDE
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menuApis.urls')),
<<<<<<< HEAD
    path('valorantApi/',include('valorantApi.urls')),
=======
    path('digimon/',include('digimonApi.urls')),
    path('makeup/',include('makeupApi.urls')),
>>>>>>> cf384d05b47dde311423b4a20d7e840f6ee5dd3c
]
