from django.db import models

# Create your models here.
class ReleaseNote(models.Model):
    release_note_id = models.AutoField(verbose_name='リリースノートID', primary_key=True, auto_created=True)
    version         = models.CharField(verbose_name='バージョン', max_length=150, null=False)
    overview        = models.TextField(verbose_name='概要', null=False)
    new_feature     = models.TextField(verbose_name='新機能', null=True, blank=True)
    improvement     = models.TextField(verbose_name='改善', null=True, blank=True)
    bug_fix         = models.TextField(verbose_name='バグ修正', null=True, blank=True)
    created_at      = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='リリースノートマスタ'
        verbose_name_plural = 'リリースノートマスタ'
    
    def __str__(self):
        return self.version


class MyCareer(models.Model):
    carrer_id         = models.AutoField(verbose_name='プロダクトID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='キャリア名', max_length=150, null=False)
    content1          = models.TextField(verbose_name='キャリア内容1', null=False)
    content2          = models.TextField(verbose_name='キャリア内容2', null=True, blank=True)
    content3          = models.TextField(verbose_name='キャリア内容3', null=True, blank=True)
    content4          = models.TextField(verbose_name='キャリア内容4', null=True, blank=True)
    content5          = models.TextField(verbose_name='キャリア内容5', null=True, blank=True)
    career_started_at = models.DateTimeField(verbose_name='キャリア開始日', null=False)
    career_ended_at   = models.DateTimeField(verbose_name='キャリア終了日', null=True, blank=True)
    created_at        = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='キャリアマスタ'
        verbose_name_plural = 'キャリアマスタ'
    
    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    skill_category_id = models.AutoField(verbose_name='スキルカテゴリ名', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='スキルカテゴリ名', max_length=150, null=False)
    created_at        = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='スキルカテゴリマスタ'
        verbose_name_plural = 'スキルカテゴリマスタ'
    
    def __str__(self):
        return self.name


class MySkill(models.Model):
    skill_id         = models.AutoField(verbose_name='スキルID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='スキル名', max_length=150, null=False)
    category          = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='category')
    created_at        = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='スキルマスタ'
        verbose_name_plural = 'スキルマスタ'
    
    def __str__(self):
        return self.name


class InterestedDomain(models.Model):
    domain_id         = models.AutoField(verbose_name='ドメインID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='興味のある領域', max_length=150, null=False)
    created_at        = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='ドメインマスタ'
        verbose_name_plural = 'ドメインマスタ'
    
    def __str__(self):
        return self.name


class Capabilities(models.Model):
    capability_id     = models.AutoField(verbose_name='資格ID', primary_key=True, auto_created=True)
    name              = models.CharField(verbose_name='資格名', max_length=150, null=False)
    created_at        = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name='資格マスタ'
        verbose_name_plural = '資格マスタ'
    
    def __str__(self):
        return self.name