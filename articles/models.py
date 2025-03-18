from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from accounts.models import *

class ArticleCategory(models.Model):
    article_category_id = models.AutoField(verbose_name='記事カテゴリID', primary_key=True, auto_created=True)
    name                = models.CharField(verbose_name='記事カテゴリ名', max_length=200, null=False)
    created_at          = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name = '記事カテゴリマスタ'
        verbose_name_plural = '記事カテゴリマスタ'
    
    def __str__(self):
        return self.name


class ViewedCount(models.Model):
    count_id     = models.AutoField(verbose_name='カウントID', primary_key=True, auto_created=True)
    viewed_count = models.IntegerField(verbose_name='ビュー回数', default=0)

    class Meta:
        verbose_name = '記事閲覧回数マスタ'
        verbose_name_plural = '記事閲覧回数マスタ'
    
    def __str__(self):
        return str(self.viewed_count)


class Article(models.Model):
    article_id     = models.AutoField(verbose_name='記事ID', primary_key=True, auto_created=True)
    author         = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='articles')
    title          = models.CharField(verbose_name='タイトル', max_length=200)
    category       = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='articles')
    content        = MarkdownxField(verbose_name='コンテンツ')
    header_img_url = models.FileField(verbose_name='ヘッダー画像格納先', upload_to='header_img/', blank=True)
    viewed_count   = models.ForeignKey(ViewedCount, on_delete=models.CASCADE, related_name='articles')
    created_at     = models.DateField(verbose_name='作成日', auto_now_add=True)
    updated_at     = models.DateField(verbose_name='更新日', auto_now=True)
    is_draft       = models.BooleanField(verbose_name='下書きフラグ', default=False)

    class Meta:
        verbose_name = '記事マスタ'
        verbose_name_plural = '記事マスタ'
    
    def get_markdownx_content(self):
        return mark_safe(markdownify(self.content))
    
    def __str__(self):
        return self.title


class Favorite(models.Model):
    user         = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='favorite')
    article      = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorite')
    favorited_at = models.DateField(verbose_name='お気に入り登録日', auto_now_add=True)

    class Meta:
        verbose_name = 'お気に入りマスタ'
        verbose_name_plural = 'お気に入りマスタ'
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"],
                name="favorite_unique"
            ),
        ]
