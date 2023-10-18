from django.shortcuts import render
from biblioteca.models import Libro
# Create your views here.
def index(request):
    return render(request,'index.html')

def listar_libros(request):
    libros = Libro.objects.select_related('biblioteca').prefetch_related("autores");
    return render(request,'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request,id_libros):
    libro = Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id=id_libros)
    return render(request,'libro/libro.html',{"libro_mostrar":libro})