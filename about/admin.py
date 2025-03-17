from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(MyCareer)
class myCareerAdmin(admin.ModelAdmin):
    list_display = ('carrer_id', 'name', 'career_started_at', 'career_ended_at',)

@admin.register(MySkill)
class MySkillAdmin(admin.ModelAdmin):
    list_display = ('skill_id', 'name', 'category',)

@admin.register(InterestedDomain)
class InterestedDomainAdmin(admin.ModelAdmin):
    list_display = ('domain_id', 'name',)

Capabilities
@admin.register(Capabilities)
class CapabilitiesAdmin(admin.ModelAdmin):
    list_display = ('capability_id', 'name',)