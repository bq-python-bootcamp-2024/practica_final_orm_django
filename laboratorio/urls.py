from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index, name='index'),
    # CRUD: Listar/leer laboratorio
    path('laboratorio/listar/', views.listar_laboratorio, name='listar_laboratorio'),
    # CRUD: Insertar laboratorio
    path('laboratorio/insertar/', views.insertar_laboratorio, name='insertar_laboratorio'),
    # CRUD: Actualizar laboratorio
    path('laboratorio/<int:id_laboratorio>/actualizar/', views.actualizar_laboratorio, name='actualizar_laboratorio'),
    # CRUD: Eliminar laboratorio
    path('laboratorio/<int:id_laboratorio>/eliminar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]