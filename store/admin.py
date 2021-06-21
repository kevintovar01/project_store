from django.contrib import admin
from .models import CategoryProduct,ProductModels

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    '''Admin View for CategoryProduct'''
    readonly_fields = ('created', 'updated')

@admin.register(ProductModels)
class ProductModelsAdmin(admin.ModelAdmin):
    '''Admin View for ProductModels'''
    readonly_fields = ('create', 'updated')