# config/urls.py
# Django and third parties modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # home
    path('', include('app.home.urls',namespace='home')),

    # admin
    path('admin/', admin.site.urls),
]
