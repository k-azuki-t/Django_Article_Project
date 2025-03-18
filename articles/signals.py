from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Article, ViewedCount

@receiver(pre_save, sender=Article)
def create_view_count_record(sender, instance, **kwargs):

    if not instance.viewed_count_id:  # 既に設定されている場合は処理しない
        viewed_count = ViewedCount.objects.create()
        instance.viewed_count = viewed_count