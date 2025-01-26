# Generated by Django 5.1.5 on 2025-01-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('TECH', 'IT技術'), ('MARKETING', 'マーケティング'), ('DESIGN', 'デザイン'), ('BLOG', 'ブログ'), ('PSYCHOLOGY', '心理学'), ('BEHAVIORAL_ECONOMICS', '行動経済学'), ('BRAIN_SCIENCE', '脳科学'), ('OTHER', 'その他')], default='TECH', max_length=200, verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='header_img_url',
            field=models.CharField(max_length=1000, verbose_name='ヘッダー画像格納先'),
        ),
    ]
