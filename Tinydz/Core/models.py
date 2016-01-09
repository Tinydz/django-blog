from django.db import models
from django.contrib.auth.models import User
from collections import OrderedDict
# Create your models here.

# 标签管理器
class TagManager(models.Manager):
    def get_Tag_list(self):
        tags = Tag.objects.all()
        tag_list = []
        for i in range(len(tags)):
            tag_list.append([])
        for i in range(len(tags)):
            temp = Tag.objects.get(name=tags[i])
            posts = temp.article_set.all()
            tag_list[i].append(tags[i].name)
            tag_list[i].append(len(posts))
        return tag_list

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=20, blank=True)
    
    objects = models.Manager()
    tagManager = TagManager()
    
    @models.permalink
    def get_absolute_url(self):
        return('TagAchieve', (), {
                'tag': self.name})
        
    def __str__(self):
        return self.name 

class CategoryManager(models.Manager):
    def get_Category_list(self):
        categories = Category.objects.all()
        category_list = []
        for i in range(len(categories)):
            category_list.append([])
        for i in range(len(categories)):
            temp = Category.objects.get(name=categories[i].name)
            posts = temp.article_set.all()
            category_list.append(categories[i])
            category_list.append(len(posts))
        return category_list

    def get_Category_article_achieve(self):
        articles = Article.objects.order_by('-publish_time')
        categories = Category.objects.all()
        category_article_list = []
        for category in categories:
            for article in articles:
                if category.name==article.category.name:
                    category_article_list.append(article)
        return category_article_list

# 月归档
class Category(models.Model):
    name = models.CharField(max_length=40)

    objects = models.Manager()
    categoryManager = CategoryManager()

    def __str__(self):
        return self.name

    
class ArticleManager(models.Manager):
    def get_Article_byDate(self):
        post_date = Article.objects.dates('publish_time', 'month')
        date_list = []
        for i in range(len(post_date)):
            date_list.append([])
        for i in range(len(post_date)):
            curyear = post_date[i].year
            curmonth = post_date[i].month
            tempArticle = Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            tempNum = len(tempArticle)
            date_list[i].append(post_date[i])
            date_list[i].append(tempNum)
        return date_list

    def get_Article_OnArchieve(self):
        post_date = Article.objects.dates('publish_time', 'month')
        post_date_article = []
        for i in range(len(post_date)):
            post_date_article.append([])
        for i in range(len(post_date)):
            curyear = post_date[i].year
            curmonth = post_date[i].month
            tempArticle = Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            post_date_article[i] = tempArticle
        dicts = OrderedDict()
        for i in range(len(post_date)):
            dicts.setdefault(post_date[i], post_date_article[i])
        return dicts

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = models.TextField(blank=True, null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    objects = models.Manager()
    articleManager = ArticleManager()

    @models.permalink
    def get_absolute_url(self):
        return('ArticleDetail', (), {
            'year':self.publish_time.year,
            'month': self.publish_time.strftime('%m'),
            'day' : self.publish_time.strftime('%d'),
            'id' : self.id
            })
     
    def get_tags(self):
        tagAll = self.tags.all()
        return tagAll

    def get_pre_article(self):
        temp = Article.objects.order_by('id')
        cur = Article.objects.get(id=self.id)
        count = 0
        for i in temp:
            if i.id == cur.id:
                index = count
                break
            else:
                count = count + 1
        if index != 0:
            return temp[index - 1]

    def get_next_article(self):
        temp = Article.objects.order_by('id')
        maxlen = len(temp) - 1
        cur = Article.objects.get(id=self.id)
        count = 0
        for i in temp:
            if i.id == cur.id:
                index = count
                break
            else:
                count = count + 1
        if index != maxlen:
            return temp[index + 1]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']




