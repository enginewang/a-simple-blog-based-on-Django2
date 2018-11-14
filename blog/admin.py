from django.contrib import admin
from . import models
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'page_views')
    list_filter = ('pub_time',)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tags)
admin.site.register(models.User)
