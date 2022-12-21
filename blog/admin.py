from django.contrib import admin
from .models import Article, Category

# create a class for customizing models in admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}

# register models in admin panel
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'str_category')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status', '-publish']

    # To fix the ManyToManyField error that says this field must be a string for list_display, we use this new method
    def str_category(self, obj):    # 'obj' is the article that called
        return [category.title for category in obj.category.all()]
    str_category.short_description = "دسته بندی"

admin.site.register(Article, ArticleAdmin)