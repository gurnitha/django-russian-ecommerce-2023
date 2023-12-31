# config/urls.py
# Django and third parties modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # home
    path('', include('app.home.urls',namespace='home')),
    # about
    path('', include('app.about.urls',namespace='about')),
    # contact
    path('', include('app.contact.urls',namespace='contact')),
    # admin
    path('admin/', admin.site.urls),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)