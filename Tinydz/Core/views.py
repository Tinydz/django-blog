from django.shortcuts import render
from Core.models import Article, Tag, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    articles = Article.objects.all()
    category_article_list = Category.categoryManager.get_Category_article_achieve()
    paginator = Paginator(articles, 4)
    page_num = request.GET.get('page')
    try:
    	articles = paginator.page(str(page_num))
    except PageNotAnInteger:
    	articles = paginator.page(1)
    except EmptyPage:
    	articles = paginator.page(paginator.num_pages)
    tagCloud = Tag.objects.all()
    return render(request, 'index.html', locals())

def ArticleDetail(request, year, month, day, id):
	try:
		article = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	tagCloud = Tag.objects.all()
	return render(request, 'articleDetail.html', locals())

def Achieve(request):
    Is_achieve = True
    articles = Article.objects.order_by('-publish_time')
    page_size = 5
    page_num = request.GET.get('page')
    paginator = Paginator(articles, page_size)
    try:
        articles = paginator.page(str(page_num))
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage :
        articles = paginator.page(paginator.num_pages)
    tagCloud = Tag.objects.all()
    return render(request, 'achieve.html', locals())

def TagAchieve(request, tag):
    Is_tagachieve = True
    tags = Tag.objects.get(name=tag)
    articles = tags.article_set.all()
    page_size = 8
    page_num = request.GET.get('page')
    paginator = Paginator(articles, page_size)
    try:
        articles = paginator.page(str(page_num))
    except PageNotAnInteger :
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    tagCloud = Tag.objects.all()
    return render(request, 'achieve.html',locals())


def CategoryAchieve(request):
    articles = Category.categoryManager.get_Category_article_achieve()
    page_size = 8
    page_num = request.GET.get('page')
    paginator = Paginator(articles, page_size)
    try:
        articles = paginator.page(str(page_num))
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    tagCloud = Tag.objects.all()
    return render(request, 'categoryachieve.html', locals())


def PictureCollection(request):
    return render(request, 'picturecollection.html')


