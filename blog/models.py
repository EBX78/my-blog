from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter

# recive data from admin panel with this template
class Article(models.Model):
    STATUS_CHOICES = (
        ('p', 'منتشر شده'),
        ('d', 'پیش نویس')
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    # change Article title name to persian name
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    # show articles by title 
    def __str__(self):
        return self.title

    # change publish datetime to local calender
    def jpublish(self):
    	return jalali_converter(self.publish)

    # change jpublish column name in articl list
    jpublish.short_description = "زمان انتشار"