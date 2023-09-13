# app/product/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.product.models import Category, Product, Images

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent', 'status','image_tag']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status','image_tag']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)