from django.contrib import admin
from django.urls import path
from Downloader.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", view_dir),
    path("show/" , show_file)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
