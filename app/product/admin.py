# app/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.product.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
