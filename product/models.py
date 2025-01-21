from django.db import models

# Create your models here.
class Product(models.Model):
    product_id     = models.IntegerField(verbose_name='プロダクトID', primary_key=True, auto_created=True)
    name           = models.CharField(verbose_name='プロダクト名', max_length=150)
    content        = models.TextField(verbose_name='コンテンツ')
    header_img_url = models.ImageField(verbose_name='ヘッダー画像格納先')
    reated_at      = models.DateField(verbose_name='登録日', auto_now_add=True)

    class Meta:
        verbose_name='プロダクトマスタ'
        verbose_name_plural = 'プロダクトマスタ'