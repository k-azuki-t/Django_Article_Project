# Generated by Django 5.1.5 on 2025-01-17 17:00

import django.db.models.deletion
import markdownx.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='記事ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('category', models.CharField(max_length=200, verbose_name='カテゴリ')),
                ('content', markdownx.models.MarkdownxField(verbose_name='コンテンツ')),
                ('header_img_url', models.ImageField(upload_to='', verbose_name='ヘッダー画像格納先')),
                ('viewed_count', models.IntegerField(default=0, verbose_name='ビュー回数')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
                ('is_draft', models.BooleanField(default=False, verbose_name='下書きフラグ')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '記事マスタ',
                'verbose_name_plural': '記事マスタ',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('tag_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='タグID')),
                ('name', models.CharField(max_length=50, verbose_name='タグ名称')),
                ('article', models.ManyToManyField(related_name='article_tag', to='articles.article')),
            ],
            options={
                'verbose_name': '記事タグマスタ',
                'verbose_name_plural': '記事タグマスタ',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_at', models.DateField(auto_now_add=True, verbose_name='お気に入り登録日')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'お気に入りマスタ',
                'verbose_name_plural': 'お気に入りマスタ',
            },
        ),
        migrations.CreateModel(
            name='UploadedFileUrl',
            fields=[
                ('file_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ファイルID')),
                ('url', models.FileField(unique=True, upload_to='', verbose_name='ファイル格納先')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_file_url', to='articles.article')),
            ],
            options={
                'verbose_name': 'アップロードファイル格納先マスタ',
                'verbose_name_plural': 'アップロードファイル格納先マスタ',
            },
        ),
    ]
