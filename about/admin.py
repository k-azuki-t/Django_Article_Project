from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ReleaseNote)
class ReleaseNoteAdmin(admin.ModelAdmin):
    list_display = ('release_note_id', 'version', 'content', 'created_at',)

@admin.register(MyCareer)
class myCareerAdmin(admin.ModelAdmin):
    list_display = ('carrer_id', 'name', 'career_started_at', 'career_ended_at',)

@admin.register(MySkill)
class MySkillAdmin(admin.ModelAdmin):
    list_display = ('skill_id', 'name', 'category',)

@admin.register(InterestedDomain)
class InterestedDomainAdmin(admin.ModelAdmin):
    list_display = ('domain_id', 'name',)

@admin.register(Capabilities)
class CapabilitiesAdmin(admin.ModelAdmin):
    list_display = ('capability_id', 'name',)

@admin.register(SkillCategory)
class SkillCategory(admin.ModelAdmin):
    list_display = ('skill_category_id', 'name',)