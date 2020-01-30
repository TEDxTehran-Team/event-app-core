from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = (
    [
        path("v1/", include("tedxapp.urls.v1")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
