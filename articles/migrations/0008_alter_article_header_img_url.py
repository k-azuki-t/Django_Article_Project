# Generated by Django 5.1.5 on 2025-02-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_header_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='header_img_url',
            field=models.FileField(upload_to='header_img/', verbose_name='ヘッダー画像格納先'),
        ),
    ]
