from django.shortcuts import render
from Core.models import Article, Tag, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, hashers, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
import time

# Create your views here.

def Login(request):
	error = None
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				print('username:', user.username)
				return HttpResponseRedirect(reverse('AdminIndex'))
			else:
				error = "用户名或密码有误, 请重新登录, ^_^ ..."
				return render(request, 'login.html', locals())
		else:
			error = "用户不存在, 请重新登录, ^_^ ..."
			return render(request, 'login.html', locals())
	elif request.method == 'GET':
		return render(request, 'login.html', locals())

@login_required(login_url='/Account/login/')
def AdminEditView(request, article_id):
	article = Article.objects.get(id=article_id)
	tags = article.get_tags()
	categories = Category.objects.all()
	# 将datetime类型转化成str
	publish_time = article.publish_time.strftime('%Y-%m-%d %H:%M:%S')
	article_tags = ''
	for tag in tags:
		article_tags += tag.name + ','
	return render(request, 'adminedit.html', locals())

@login_required(login_url='/Account/login/')
def AdminCreate(request):
	userobj = User.objects.get(username=request.user.username)
	# 默认分类为空
	ctg = Category()
	publish_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
	ctg.save()
	article = Article(title='默认标题', content='##保存井号，输入标题', category=ctg, author=userobj, publish_time=publish_time)
	article.save()
	return HttpResponseRedirect(reverse('AdminEditView', args=[article.id]))

@login_required(login_url='/Account/login/')
def AdminDeploy(request):
	title = request.POST['title']
	id = request.POST['article_id']
	category = request.POST['category']
	content = request.POST['content']
	publish_time_str = request.POST['publish_time']
	# 将str字符时间转换成日期型
	publish_time = datetime.fromtimestamp(time.mktime(time.strptime(publish_time_str, "%Y-%m-%d %H:%M:%S")))
	tags = request.POST['tags']
	tags_arr = tags.split(',')
	tags_arr = list(set(tags_arr))
	print('alltag', Tag.objects.all())
	article = Article.objects.get(id=id)
	article.title = title
	article.category = Category.objects.get(name=category)
	article.content = content
	article.publish_time = publish_time
	article.tags.all().delete()
	for tagname in tags_arr:
		if tagname != '':
			tagobj = None
			try:
				tagobj = Tag.objects.get(name=tagname)
				print('tagobj: ', tagobj)
			except:
				print('wrong....')
				tagobj = Tag(name=tagname)
				tagobj.save()
			article.tags.add(tagobj)

	article.save()
	return HttpResponseRedirect(reverse('AdminIndex'))


@login_required(login_url='/Account/login/')
def AdminIndex(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 8)
	page_num = request.GET.get('page')
	try:
		articles = paginator.page(str(page_num))
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render(request, 'adminIndex.html', locals())

@login_required(login_url='/Account/login/')
def Logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/Account/login/')

@login_required(login_url='/Account/login/')
def AdminDeleteArticle(request, article_id):
	article = Article.objects.filter(id = article_id)
	article.delete()
	return HttpResponseRedirect('/Account/AdminIndex/')

