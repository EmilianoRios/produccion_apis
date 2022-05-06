from django.urls import path
from makeupApi import views

urlpatterns = [
    path('', views.MakeUpApiAll, name ="indexMakeup"),
    path('<type_p>', views.MakeUpApi, name ="index_tipo"),
    path('<type_p>/<str:tag>',views.MakeupApiTag, name="index_tipo_tag"),
]
