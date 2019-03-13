from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Dish, Norm, Output


class NormInline(admin.TabularInline):
    model = Norm
    min_num = 2


class OutputInline(admin.TabularInline):
    model = Output
    min_num = 2


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'dish_type', 'products')
    list_display = ('name', 'dish_type', 'products_count', 'norms_count')
    list_filter = ('dish_type',)
    filter_horizontal = ('products',)
    inlines = (OutputInline, NormInline)

    def products_count(self, obj):
        return obj.products.all().count()

    def norms_count(self, obj):
        return obj.norms.all().count()

    norms_count.short_description = _('Number of Products Norms')  # type: ignore
    products_count.short_description = _('Number of Products')  # type: ignore
