# app/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.product.models import Category

admin.site.register(Category)
