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
    path('valorantApi/',include('valorantApi.urls')),
]
