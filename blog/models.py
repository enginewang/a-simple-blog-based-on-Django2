from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone


class Tags(models.Model):
    name = models.CharField('文章标签', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField('文章标题', max_length=30)
    content = MDTextField('文章内容', null=True)
    pub_time = models.DateField('发布时间', null=True, default=timezone.now)
    page_views = models.BigIntegerField('阅读量', default=0)
    CAT_CHOICES = (
        ('tech', 'Tech'),
        ('design', 'Design'),
        ('life', 'Life'),
        ('tips', 'Tips'),
        ('resource', 'Resource'),
    )
    synopsis = models.TextField('文章概要', null=True, max_length=200, default=" ")
    category = models.CharField('文章类别', null=True, max_length=15, choices=CAT_CHOICES)
    tag = models.ManyToManyField(Tags, verbose_name='文章标签')
    next_id = models.IntegerField(default=0)
    prev_id = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    class Meta:
        ordering = ('title', )
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(null=True, blank=True, max_length=15)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=25, default='匿名用户')
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ('time', )
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:20]


class Count(models.Model):
    blog_num = models.IntegerField(default=0)
    tag_num = models.IntegerField(default=0)
    visitor_num = models.IntegerField(default=0)

    class Meta:
        verbose_name = '数量统计'
        verbose_name_plural = verbose_name