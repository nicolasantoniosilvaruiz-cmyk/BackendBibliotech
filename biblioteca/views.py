from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, 'biblioteca/detalle_libro.html', {'libro': libro})

def libros_por_categoria(request, cat):
    libros = Libro.objects.filter(categoria=cat)
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros, 'categoria_actual': cat})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})