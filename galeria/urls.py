#galeira urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from galeria import views

urlpatterns = [
    path('', views.imagen_list, name='imagen_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)