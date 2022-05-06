from tokenize import Name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='InicioNoticias'),
    path('filtro/<categoria>', views.filtro, name='Filtro'),
    path('noticia/<title>', views.noticia, name='Noticia'),

]

