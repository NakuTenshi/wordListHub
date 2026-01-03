from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Downloader.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", view_dir, name="home"),
    path("upload/", uploadWordlist, name="upload"),
    path("show/", show_file, name="show"),


    path("api/get_dirs", get_dirs_api, name="get_dirs")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
