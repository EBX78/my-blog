from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status')    # show article info and sort with this info
    list_filter = ('publish', 'status')    # filter articles
    search_fields = ('title', 'description')    # add search field
    prepopulated_fields = {'slug':('title',)}    # auto fill 'slug' field with 'title' content
    ordering = ['status', '-publish']    # set default sort for articles

admin.site.register(Article, ArticleAdmin)    # register models in admin panel