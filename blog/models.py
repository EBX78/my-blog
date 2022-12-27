from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='أیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('p', 'منتشر شده'),
        ('d', 'پیش نویس')
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, blank=True, verbose_name='دسته بندی')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def jpublish(self):
    	return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
    
    def str_category(self):
        return [cat.title for cat in self.category.all()]
    str_category.short_description = "دسته بندی"