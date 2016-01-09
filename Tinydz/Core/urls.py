'''
Created on 2015-11-22

@author: AndrewsMJ
'''
from django.conf.urls import url, patterns
from . import feeds

urlpatterns = patterns('',
    url(r'^index/$', 'Core.views.index', name='index'),
    url(r'^aritcle/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'Core.views.ArticleDetail', name='ArticleDetail'),
    url(r'^achieves/$', 'Core.views.Achieve', name="Achieve"),
    url(r'^tagachieves/(?P<tag>\w+)/$', 'Core.views.TagAchieve', name='TagAchieve'),
    url(r'^feed/$', feeds.MyRSSFeed(), name="RSS"),
    url(r'^categoryachieve/$', 'Core.views.CategoryAchieve', name='CategoryAchieve'),
    url(r'^picture/$', 'Core.views.PictureCollection', name='picture'),
)


