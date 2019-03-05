from django.contrib import admin

from .models import AgeCategory, DishType, Group, ProductCategory


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass
