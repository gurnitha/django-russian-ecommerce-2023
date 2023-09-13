# app/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.product.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status']
    list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)