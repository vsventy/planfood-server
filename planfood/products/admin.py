from django.contrib import admin

from .models import Norm, Product


class NormInline(admin.TabularInline):
    model = Norm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_number', 'name')
    inlines = [NormInline]


@admin.register(Norm)
class NormAdmin(admin.ModelAdmin):
    list_display = ('product', 'age_category', 'group', 'value')
