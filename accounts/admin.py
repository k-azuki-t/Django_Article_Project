from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ServiceUser)
class ServiceUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'last_login', 'created_at', )