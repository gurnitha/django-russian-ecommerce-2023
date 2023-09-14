# app/contact/urls.py
# Django and third parties modules
from django.urls import path

# Locals
from app.contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='contactpage'),
]
