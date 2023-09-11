# app/home/urls.py
# Django and third parties modules
from django.urls import path

# Locals
from app.home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='homepage'),
]
