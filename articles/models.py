from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from accounts.models import *

CATEGORY_CHOICES = [
    ('TECH', 'IT技術'),
    ('MARKETING', 'マーケティング'),
    ('DESIGN', 'デザイン'),
    ('BLOG', 'ブログ'),
    ('PSYCHOLOGY', '心理学'),
    ('BEHAVIORAL_ECONOMICS', '行動経済学'),
    ('BRAIN_SCIENCE', '脳科学'),
    ('OTHER', 'その他'),
]

class Article(models.Model):
    article_id     = models.IntegerField(verbose_name='記事ID', primary_key=True, auto_created=True)
    author         = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='article')
    title          = models.CharField(verbose_name='タイトル', max_length=200)
    category       = models.CharField(verbose_name='カテゴリ', max_length=200, choices=CATEGORY_CHOICES, default='TECH')
    content        = MarkdownxField(verbose_name='コンテンツ')
    header_img_url = models.FileField(verbose_name='ヘッダー画像格納先', upload_to='header_img/', blank=True)
    viewed_count   = models.IntegerField(verbose_name='ビュー回数', default=0)
    created_at     = models.DateField(verbose_name='作成日', auto_now_add=True)
    updated_at     = models.DateField(verbose_name='更新日', auto_now=True)
    is_draft       = models.BooleanField(verbose_name='下書きフラグ', default=False)

    class Meta:
        verbose_name = '記事マスタ'
        verbose_name_plural = '記事マスタ'
    
    def get_markdownx_content(self):
        return mark_safe(markdownify(self.content))


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
