# galeria/models.py
from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=[
        ('camara', 'Cámara'),
        ('descargas', 'Descargas'),
        ('whatsapp', 'WhatsApp'),
        ('otros', 'Otros'),
    ])
    imagen = models.ImageField(upload_to='imagenes/')
    fecha_subida = models.DateTimeField(auto_now_add=True)  # Agregar este campo

    def __str__(self):
        return self.nombre