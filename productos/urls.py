from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-producto', views.agregar_producto, name='agregar_producto'),
    path('listar-productos', views.listar_productos, name='listar_productos'),
    path('editar-producto/<int:id>', views.editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('registro', views.registro, name='registro'),
   
    
]