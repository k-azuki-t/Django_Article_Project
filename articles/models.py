from django.db import models
from markdownx.models import MarkdownxField
from django.contrib.auth.hashers import make_password
from accounts.models import *

# Create your models here.
# class ServiceUser(models.Model):
#     user_id    = models.IntegerField(verbose_name='ユーザーID', primary_key=True, auto_created=True)
#     name       = models.CharField(verbose_name='ユーザー名', max_length=150)
#     email      = models.EmailField(verbose_name='メールアドレス', unique=True, null=False, blank=False)
#     password   = models.CharField(verbose_name='パスワード', max_length=128)
#     last_login = models.DateField(verbose_name='最終ログイン')
#     created_at = models.DateField(verbose_name='登録日', auto_now_add=True)
#     updated_at = models.DateField(verbose_name='更新日', auto_now=True)
#     # is_deleted = models.BooleanField(verbose_name='削除フラグ')
#     is_creator   = models.BooleanField(verbose_name='クリエイターフラグ', default=False)

#     class Meta:
#         verbose_name = 'ユーザーマスタ'
#         verbose_name_plural = 'ユーザーマスタ'

#     def set_password(self, input_password):
#         self.password = make_password(input_password)
#         self.save()


class Article(models.Model):
    article_id     = models.IntegerField(verbose_name='記事ID', primary_key=True, auto_created=True)
    author         = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='article')
    title          = models.CharField(verbose_name='タイトル', max_length=200)
    category       = models.CharField(verbose_name='カテゴリ', max_length=200)
    content        = MarkdownxField(verbose_name='コンテンツ')
    header_img_url = models.ImageField(verbose_name='ヘッダー画像格納先')
    viewed_count   = models.IntegerField(verbose_name='ビュー回数', default=0)
    created_at     = models.DateField(verbose_name='作成日', auto_now_add=True)
    updated_at     = models.DateField(verbose_name='更新日', auto_now=True)
    is_draft       = models.BooleanField(verbose_name='下書きフラグ', default=False)
    # is_deleted     = models.BooleanField(verbose_name='削除フラグ')

    class Meta:
        verbose_name = '記事マスタ'
        verbose_name_plural = '記事マスタ'


class UploadedFileUrl(models.Model):
    file_id = models.IntegerField(verbose_name='ファイルID', primary_key=True, auto_created=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='uploaded_file_url')
    url     = models.FileField(verbose_name='ファイル格納先', unique=True, null=False)

    class Meta:
        verbose_name = 'アップロードファイル格納先マスタ'
        verbose_name_plural = 'アップロードファイル格納先マスタ'


class ArticleTag(models.Model):
    tag_id  = models.IntegerField(verbose_name='タグID', primary_key=True, auto_created=True)
    article = models.ManyToManyField(Article, related_name='article_tag')
    name    = models.CharField(verbose_name='タグ名称', max_length=50)

    class Meta:
        verbose_name = '記事タグマスタ'
        verbose_name_plural = '記事タグマスタ'


class Favorite(models.Model):
    user         = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='favorite')
    article      = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorite')
    favorited_at = models.DateField(verbose_name='お気に入り登録日', auto_now_add=True)

    class Meta:
        verbose_name = 'お気に入りマスタ'
        verbose_name_plural = 'お気に入りマスタ'
