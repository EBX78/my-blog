from django.contrib import admin
from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'status']
    list_filter = ['status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-position']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'jpublish', 'status', 'str_category']
    list_filter = ['publish', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-id']