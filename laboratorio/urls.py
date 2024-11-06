from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    path('laboratorio/listar/', views.listar_laboratorio, name='listar_laboratorio'),
    path('laboratorio/insertar/', views.insertar_laboratorio, name='insertar_laboratorio'),
    path('laboratorio/<int:id_laboratorio>/actualizar/', views.actualizar_laboratorio, name='actualizar_laboratorio'),
    path('laboratorio/<int:id_laboratorio>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]