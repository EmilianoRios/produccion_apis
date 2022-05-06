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
    path('valorant/',include('valorantApi.urls')),
    path('digimon/',include('digimonApi.urls')),
    path('makeup/',include('makeupApi.urls')),
    path('breakingbad/',include('breakingbadApi.urls')),
    path('disney/',include('disneyApi.urls')),
    path('freetogame/',include('freeToGameApi.urls')),
    path('noticias/',include('noticiasApi.urls')),
    path('covid/',include('covidApi.urls')),
]
