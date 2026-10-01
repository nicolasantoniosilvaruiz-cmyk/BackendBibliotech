from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('categoria/<str:cat>/', views.libros_por_categoria, name='libros_por_categoria'),
    path('nuevo/', views.agregar_libro, name='agregar_libro'),
]