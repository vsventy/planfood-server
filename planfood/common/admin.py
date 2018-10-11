from django.contrib import admin

from .models import AgeCategory, Group


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
