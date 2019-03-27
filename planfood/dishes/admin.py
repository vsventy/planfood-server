from django.contrib import admin
from django.core.management import call_command
from django.utils.translation import ugettext_lazy as _

from .models import Dish, Norm, Output


class NormInline(admin.TabularInline):
    model = Norm


class OutputInline(admin.TabularInline):
    model = Output


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'dish_type', 'products')
    list_display = (
        'name',
        'dish_type',
        'products_count',
        'outputs_count',
        'norms_count',
    )
    list_filter = ('dish_type',)
    filter_horizontal = ('products',)
    inlines = (OutputInline, NormInline)
    actions = ['create_norms', 'create_outputs']
    actions_without_queryset = ['create_norms', 'create_outputs']

    def products_count(self, obj):
        return obj.products.all().count()

    def norms_count(self, obj):
        return '{} ({})'.format(
            obj.norms.all().count(), obj.norms.filter(value=0).count()
        )

    def outputs_count(self, obj):
        return '{} ({})'.format(
            obj.outputs.all().count(), obj.outputs.filter(value='0').count()
        )

    def create_norms(self, request, queryset):
        call_command('create_norms')

    def create_outputs(self, request, queryset):
        call_command('create_outputs')

    norms_count.short_description = _('Number of Products Norms')  # type: ignore
    outputs_count.short_description = _('Number of Products Outputs')  # type: ignore
    products_count.short_description = _('Number of Products')  # type: ignore
    create_norms.short_description = _(
        'Creates empty norms for all dishes'
    )  # type: ignore
    create_outputs.short_description = _(
        'Creates empty outputs for all dishes'
    )  # type: ignore
