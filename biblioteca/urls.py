from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('libros/listar',views.listar_libros,name='lista_libros'),
    path('libros/<int:id_libros>/',views.dame_libro,name="dame_libro"),
]
