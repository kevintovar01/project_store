from django.contrib import admin
from .models import Category, Post
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for '''
    readonly_fields = ('created', 'updated')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''
    readonly_fields = ('created', 'updated')
