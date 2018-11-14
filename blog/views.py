from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import markdown
from django.views.generic import View, ListView
from pure_pagination.mixins import PaginationMixin
from pure_pagination import Paginator, PageNotAnInteger


class ModelListView(PaginationMixin, ListView):
    paginate_by = 10
    object = models.Article


def homepage(request):
    return render(request, 'homepage.html')


def blog_index(request):
    all_articles = models.Article.objects.all()
    article_num = all_articles.count()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_articles, request=request, per_page=6)
    articles = p.page(page)
    return render(request, 'blog_index.html', {
        'articles': articles,
        'article_num': article_num,
    })


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    article.content = markdown.markdown(article.content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    article.next_id = str(int(article_id) + 1)
    article.prev_id = str(int(article_id) - 1)
    article.number = models.Article.objects.all().count()
    return render(request, 'article_page.html', {'article': article})


def edit_page(request, article_id):
    if article_id == '0':
        return render(request, 'edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', 0)
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog_index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'article_page.html', {'article': article})