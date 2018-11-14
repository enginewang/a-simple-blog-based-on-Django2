# -*- coding = 'utf-8' -*-
from haystack import indexes
from blog.models import Article
import datetime


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_time__lte=datetime.datetime.now())
