# app/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.home.models import Setting

admin.site.register(Setting)