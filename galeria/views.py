# galeria/views.py
from django.shortcuts import render
from .models import Imagen

def galeria(request):
    imagenes = Imagen.objects.all()  # Obtener todas las imágenes
    imagenes_por_categoria = {}

    # Organizar las imágenes por categoría
    for imagen in imagenes:
        if imagen.categoria not in imagenes_por_categoria:
            imagenes_por_categoria[imagen.categoria] = []
        imagenes_por_categoria[imagen.categoria].append(imagen)

    return render(request, 'galeria/imagen_list.html', {'imagenes_por_categoria': imagenes_por_categoria})