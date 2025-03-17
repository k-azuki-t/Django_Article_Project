# Generated by Django 5.1.5 on 2025-03-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capabilities',
            fields=[
                ('capability_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='資格ID')),
                ('name', models.CharField(max_length=150, verbose_name='資格名')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
            ],
            options={
                'verbose_name': '資格マスタ',
                'verbose_name_plural': '資格マスタ',
            },
        ),
        migrations.CreateModel(
            name='InterestedDomain',
            fields=[
                ('domain_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ドメインID')),
                ('name', models.CharField(max_length=150, verbose_name='興味のある領域')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
            ],
            options={
                'verbose_name': 'ドメインマスタ',
                'verbose_name_plural': 'ドメインマスタ',
            },
        ),
        migrations.CreateModel(
            name='MyCareer',
            fields=[
                ('carrer_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='プロダクトID')),
                ('name', models.CharField(max_length=150, verbose_name='キャリア名')),
                ('content1', models.TextField(verbose_name='キャリア内容1')),
                ('content2', models.TextField(verbose_name='キャリア内容2')),
                ('content3', models.TextField(verbose_name='キャリア内容3')),
                ('content4', models.TextField(verbose_name='キャリア内容4')),
                ('content5', models.TextField(verbose_name='キャリア内容5')),
                ('career_started_at', models.DateField(verbose_name='キャリア開始日')),
                ('career_ended_at', models.DateField(verbose_name='キャリア終了日')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
            ],
            options={
                'verbose_name': 'キャリアマスタ',
                'verbose_name_plural': 'キャリアマスタ',
            },
        ),
        migrations.CreateModel(
            name='mySkill',
            fields=[
                ('skill_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='プロダクトID')),
                ('name', models.CharField(max_length=150, verbose_name='スキル名')),
                ('category', models.TextField(verbose_name='スキルカテゴリ')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
            ],
            options={
                'verbose_name': 'スキルマスタ',
                'verbose_name_plural': 'スキルマスタ',
            },
        ),
    ]
