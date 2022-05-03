*** ACLARACIONES *** 

* ! Vamos a trabajar con UNA sola APP por API, es decir, la API con la cual trabajes solo va tener UNA APP y todos sus templates,static y urls estarán dentro.
* ! UNA APP no debe de acceder a otras APP, SOLO se trabajará dentro.
* ! La carpeta del proyecto principal llamada “myapis” SOLO utilizaremos el archivo “urls.py”.
* ! El archivo “settings.py” del proyecto (“myapis”) SOLO se modificará las INSTALLED_APPS para agregar la APP con tu API trabajada.
* ! UTILIZAREMOS LA NOMENCLATURA camelCase o CamelCase.
Es una práctica de escritura que consiste en la unión de dos o más palabras sin espacios entre ellas, pero las diferencian una letra mayúscula inicial a partir de la segunda palabra, por ejemplo: miNombreEs.

Este nombre está dado porque forman con las letras mayúsculas iniciales la estructura de un camello que sube cuando hay un inicio de palabra y baja durante su definición.

*** POWERSHELL NO PERMITE EJECUCION DE SCRIPTS ENTORNO VIRTUAL ***

1. Ejecutar powershell e introducir lo siguiente: Set-ExecutionPolicy RemoteSigned -Force
2. Usar la convinación de teclas "win + r" e introducir -> gpedit.msc
3. Ir a la Configuración del equipo -> Plantillas administrativas -> Componentes de Windows -> Windows PowerShell
4. Hacer doble click en el archivo "Activar la ejecución de scripts"
5. En el apartado de opciones y en directiva de ejecución seleccionar "Permitir solo scripts firmados"

Tutorial: https://www.youtube.com/watch?v=zUszm-f6Xq4

*** CREAR UNA APP para la API ***

¡¡¡ ATENCIÓN !!!

Recuerden que "nameApi" es un nombre de ejemplo, acá deberia de estar el nombre de su API. 
Lo mismo aplica para "home" o "padre.html","hijo.html". Son solo ejemplos

¡¡¡ ATENCIÓN !!!

PASOS:

1. Dentro del terminal activaremos nuestro entorno virtual:
    -> cd venv/Scripts
    -> .\activate
  x2-> cd.. 
    # Este ultimo comando es para volver a nuestra carpeta del repositorio.
    -> cd myapis

    # Luego crearemos la APP y RECORDAR estar en la ruta del proyecto donde se encuentra "manage.py" Documents\GitHub\produccion_apis\myapis>
    -> py manage.py startapp nameApi

    # En caso de equivocarse del nombre de la APP o API clonar denuevo el repositorio desde el terminal.
    -> git clone https://github.com/EmilianoRios/produccion_apis.git

2. Crear dentro de la APP el archivo "urls.py".

**********************************************************************************
    
from django.urls import path
from nameApi import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    path('',views.home,name="Home"),
]

    # Esta es la estructura que debe tener el archivo "urls.py" dentro de tu APP.

**********************************************************************************

3. Crear en la raiz de la APP la carpeta "templates" y dentro de ella la carpeta con el nombre de la API "nameApi".

    - templates
        - nameApi
             home.html
    
    # La carpeta templates deberia de quedar asi y dentro de nameApi deberá estar todos tus archivos HTML.
    # En caso de querer hacer un HTML padre deberás llamar a este de la siguiente manera {% extends 'nameApi/padre.html' %}

4. Crear en la raiz de la APP la carpeta llamada "static" y dentro de ella la carpeta con el nombre de la API "nameApi" dentro de la carpeta "nameApi" crear las carpetas "css","js","img".

    - static
        - nameApi
            - css
                styles.css
            - js
                javaScript.js
            - img
                imagen.png

    # La carpeta static deberia de quedar asi y dentro de nameApi deberá estar todos tus archivos estaticos en sus respectivas carpetas.
    # En caso de querer llamar a uno de estos archivos dentro de tu HTML deberás cargar los archivos estaticos primero, esto al principio antes de la estructura HTML de la siguiente manera {% load static %} luego para llamar al archivo deberas de utilizar la siguiente etiqueta DJANGO {% staic 'nameApi/css/ejemplo.css' %} esto te devolverá la ruta de tu archivo para que puedas utilizarlo.

5. CREAR LAS VIEWS 

def home(request):
    return render(request,'nameApi/home.html')


6. HTML PADRE

I. Puedes utilizar la siguiente estructura para tu HTML padre.

**********************************************************************************

<!doctype html>
<html lang="es">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>{% block title %}{% endblock %}</title>
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
  <footer>
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </footer>
</html>

**********************************************************************************

II. Para hacer la herencia del HTML padre deberás de hacer lo siguiente en tu HTML HIJO.

**********************************************************************************

{% extends 'nameApi/padre.html' %} 

{% load static %}

{% block title %} 

<!-- Aqui podrás colocar el titulo de la pestaña del navegador -->

{% endblock %} 

{% block content %}

<!-- Aqui deberás de hacer tu estructura HTML -->

<div class="container">

    <p>Contenido Hijo</p>

</div>

{% endblock %}

**********************************************************************************


7. CARGAR LA APP EN "settings.py" DEL PROYECTO PRINCIPAL "myapis".

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nameApi',
]



8. EJECUTAR SERVIDOR Y TESTEAR

1. Testear la API:
    -> py manage.py runserver
    # Si la API funciona perfectamente realizar el push, si no, resolver los problemas y luego pushear.

2. Realizar el push.
    #Primero nos fijaremos si estamos en la ruta de nuestro repositorio en nuestro terminal "Documents\GitHub\produccion_apis\" recordar no estar dentro de "myapis". Luego de verificarlo realizaremos los siguientes comandos en el terminal.
    -> git status -s 
    -> git add .
    -> git commit -m 'PrimerCommit'
    -> git push origin main