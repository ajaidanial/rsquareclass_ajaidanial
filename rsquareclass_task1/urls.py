from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", view=admin.site.urls, name="admin urls"),
    path("", view=include("main_app.urls"), name="main_app urls"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
