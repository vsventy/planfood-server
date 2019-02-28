from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Dish, Norm, Output


class NormInline(admin.TabularInline):
    model = Norm


class OutputInline(admin.TabularInline):
    model = Output


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'dish_type', 'products')
    list_display = ('name', 'dish_type', 'products_count')
    list_filter = ('dish_type',)
    filter_horizontal = ('products',)
    inlines = (OutputInline, NormInline)

    def products_count(self, obj):
        return obj.products.all().count()

    products_count.short_description = _('Number of Products')  # type: ignore


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('dish', 'age_category', 'group', 'value')


@admin.register(Norm)
class NormAdmin(admin.ModelAdmin):
    list_display = ('dish', 'product', 'age_category', 'group', 'value')
