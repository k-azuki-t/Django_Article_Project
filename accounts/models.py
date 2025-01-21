from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUserManager(BaseUserManager):

    # `**extra_fields` is synonymous with `**kwargs`
    # If you define custom_fields, you can use these fields in these methods
    def create_user(self, email, password=None, **extra_fields): 
        if not email:
            raise ValueError('The Email field must be set')
        if not extra_fields.get('name'):
            raise ValueError('The name field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) # specify db
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class ServiceUser(AbstractBaseUser, PermissionsMixin):
    user_id      = models.IntegerField(verbose_name='ユーザーID', primary_key=True, auto_created=True)
    name         = models.CharField(verbose_name='ユーザー名', max_length=150)
    email        = models.EmailField(verbose_name='メールアドレス', unique=True, null=False, blank=False)
    password     = models.CharField(verbose_name='パスワード', max_length=128)
    last_login   = models.DateField(verbose_name='最終ログイン', auto_now_add=True)
    created_at   = models.DateField(verbose_name='登録日', auto_now_add=True)
    updated_at   = models.DateField(verbose_name='更新日', auto_now=True)
    # is_deleted = models.BooleanField(verbose_name='削除フラグ')
    is_creator   = models.BooleanField(verbose_name='クリエイターフラグ', default=False)
    is_staff     = models.BooleanField(verbose_name='管理者フラグ', default=False)
    is_active    = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'ユーザーマスタ'
        verbose_name_plural = 'ユーザーマスタ'

    def set_password(self, input_password):
        self.password = make_password(input_password)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []