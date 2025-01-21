from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Article, UploadedFileUrl, ArticleTag, Favorite])

# change admin site title
admin.site.site_header = 'あずきの記事管理サイト'
admin.site.site_title = 'あずきの記事'
admin.site.index_title = 'あずきの記事管理サイト'