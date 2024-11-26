# config/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from galeria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.galeria, name='galeria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Servir archivos media