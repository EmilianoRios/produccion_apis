from django.contrib import admin
from django.urls import path
from makeupApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MakeUpApiAll, name ="index"),
    path('<type_p>', views.MakeUpApi, name ="index_tipo"),
    path('<type_p>/<str:tag>',views.MakeupApiTag, name="index_tipo_tag"),
]
