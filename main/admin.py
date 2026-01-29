from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display - те параметры, которые есть в модели и будут отображаться в админке
    list_display = ['name', 'slug']
    # prepopulated_fields - поля, которые будут заполнены автоматически
    prepopulated_fields =  { 'slug': ('name', ) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available', ]
    prepopulated_fields = { 'slug': ('name', ) }

# python manage.py createsuperuser