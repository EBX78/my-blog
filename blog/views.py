from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# view of home page
def home(request):
	context = {
		'articles': Article.objects.filter(status='p'),    # get articles from model, for display in template
		'categories': Category.objects.filter(status=True)
	}
	return render(request, 'blog/home.html', context)

# view of each article page
def detail(request, slug):
	context = {
		'article': get_object_or_404(Article, slug=slug, status='p'),    # get the article that called as slug in url with 404 erorr handler
		'categories': Category.objects.filter(status=True)
	}
	return render(request, 'blog/detail.html', context)