from django.contrib import admin
from .models import *

# Register your models here.

# change admin site title
admin.site.site_header = 'あずきの記事管理サイト'
admin.site.site_title = 'あずきの記事'
admin.site.index_title = 'あずきの記事管理サイト'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'author', 'title', 'category', 'viewed_count',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'favorited_at',)