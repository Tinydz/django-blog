from django.contrib.syndication.views import Feed
from Core.models import Article

class MyRSSFeed(Feed) :
    title = "RSS feed - Welcome To Tinydz's Blog"
    link = "/feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-publish_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.publish_time

    def item_description(self, item):
        return item.content
