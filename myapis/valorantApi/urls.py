from django.urls import path
from valorantApi import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    path('',views.agents,name="Agents"),
    path('weapons/',views.weapons,name="Weapons"),
    path('weaponsSkins/',views.weaponsSkins,name="WeaponsSkins"),
    path('weaponsSkins/<str:chromas>',views.weaponsSkins,name="WeaponsChromas"),
]