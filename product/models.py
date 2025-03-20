from django.db import models

# Create your models here.
class Product(models.Model):
    product_id     = models.AutoField(verbose_name='プロダクトID', primary_key=True, auto_created=True)
    name           = models.CharField(verbose_name='プロダクト名', max_length=150, null=False)
    content        = models.TextField(verbose_name='コンテンツ', null=False)
    header_img_url = models.ImageField(verbose_name='ヘッダー画像格納先', upload_to='product_images/', null=False)
    access_url    = models.CharField(verbose_name='リンク先', max_length=150, null=False)
    created_at     = models.DateTimeField(verbose_name='登録日', auto_now_add=True, null=False)

    class Meta:
        verbose_name='プロダクトマスタ'
        verbose_name_plural = 'プロダクトマスタ'