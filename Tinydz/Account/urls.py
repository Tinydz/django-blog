
from django.conf.urls import url, patterns
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    # 使用@login_required时过滤时配置
	url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'login.html' }),
	url(r'^logout/$', 'Account.views.Logout',name='logout'),
	url(r'^AdminEditView/(?P<article_id>\d+)/$', 'Account.views.AdminEditView', name='AdminEditView'),
	url(r'^AdminIndex/$', 'Account.views.AdminIndex', name='AdminIndex'),
	url(r'^AdminDelete/(?P<article_id>\d+)/$', 'Account.views.AdminDeleteArticle', name='AdminDelete'),
	url(r'^AdminDeploy/$', 'Account.views.AdminDeploy', name='AdminDeploy'),
	url(r'^AdminCreate/$', 'Account.views.AdminCreate', name='AdminCreate'),
)
