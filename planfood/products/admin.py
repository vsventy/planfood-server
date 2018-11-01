from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Norm, Product


class NormInline(admin.TabularInline):
    model = Norm


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('item_number', 'name', 'unit', 'unit_price')


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('item_number', 'name')
    resource_class = ProductResource
    inlines = [NormInline]


@admin.register(Norm)
class NormAdmin(admin.ModelAdmin):
    list_display = ('product', 'age_category', 'group', 'value')
