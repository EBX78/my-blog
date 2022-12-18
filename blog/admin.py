from django.contrib import admin
from .models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')    # show category info and sort with this info
    list_filter = (['status'])    # filter categories
    search_fields = ('title', 'slug')    # add search field
    prepopulated_fields = {'slug':('title',)}    # auto fill 'slug' field with 'title' content

admin.site.register(Category, CategoryAdmin)    # register models in admin panel

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'scategory')    # show article info and sort with this info
    list_filter = ('publish', 'status')    # filter articles
    search_fields = ('title', 'description')    # add search field
    prepopulated_fields = {'slug':('title',)}    # auto fill 'slug' field with 'title' content
    ordering = ['status', '-publish']    # set default sort for articles

    def scategory(self, obj):
        return [category.title for category in obj.category.all()]
    scategory.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)    # register models in admin panel