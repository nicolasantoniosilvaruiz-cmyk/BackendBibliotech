from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'autor', 'categoria', 'precio_prestamo', 'stock_copias', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('titulo', 'autor', 'isbn')