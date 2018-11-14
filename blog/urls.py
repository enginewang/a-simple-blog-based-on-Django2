from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    re_path('^$', views.blog_index, name='blog_index'),
    re_path('^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    re_path(r'^edit/action/$', views.edit_action, name='edit_action'),
    # re_path('^search/', include('haystack.urls')),
]