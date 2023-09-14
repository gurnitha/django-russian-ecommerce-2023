# app/about/urls.py
# Django and third parties modules
from django.urls import path

# Locals
from app.about import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about, name='aboutpage'),
]
