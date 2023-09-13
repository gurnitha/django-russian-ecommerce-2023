# config/urls.py
# Django and third parties modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # home
    path('', include('app.home.urls',namespace='home')),

    # admin
    path('admin/', admin.site.urls),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)