from django.db import models

SKILL_CATEGORY_CHOICES = [
    ('FRONTEND', 'フロントエンド'),
    ('BACKEND', 'バックエンド'),
    ('OS/DB', 'OS・DB'),
    ('INFRASTRUCTURE', 'インフラ'),
    ('OTHER', 'その他'),
]

# Create your models here.
class MyCareer(models.Model):
    carrer_id         = models.IntegerField(verbose_name='プロダクトID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='キャリア名', max_length=150, null=False)
    content1          = models.TextField(verbose_name='キャリア内容1')
    content2          = models.TextField(verbose_name='キャリア内容2')
    content3          = models.TextField(verbose_name='キャリア内容3')
    content4          = models.TextField(verbose_name='キャリア内容4')
    content5          = models.TextField(verbose_name='キャリア内容5')
    career_started_at = models.DateField(verbose_name='キャリア開始日', null=False)
    career_ended_at   = models.DateField(verbose_name='キャリア終了日')
    created_at        = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='キャリアマスタ'
        verbose_name_plural = 'キャリアマスタ'


class mySkill(models.Model):
    skill_id         = models.IntegerField(verbose_name='プロダクトID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='スキル名', max_length=150, null=False)
    category          = models.TextField(verbose_name='スキルカテゴリ', null=False, choices=SKILL_CATEGORY_CHOICES)
    created_at        = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='スキルマスタ'
        verbose_name_plural = 'スキルマスタ'


class InterestedDomain(models.Model):
    domain_id         = models.IntegerField(verbose_name='ドメインID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='興味のある領域', max_length=150, null=False)
    created_at        = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='ドメインマスタ'
        verbose_name_plural = 'ドメインマスタ'


class Capabilities(models.Model):
    capability_id     = models.IntegerField(verbose_name='資格ID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='資格名', max_length=150, null=False)
    created_at        = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='資格マスタ'
        verbose_name_plural = '資格マスタ'