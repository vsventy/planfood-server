from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from planfood.common.models import Group
from .models import Dish, Norm, Output


class NormInline(admin.TabularInline):
    model = Norm


class OutputInline(admin.TabularInline):
    model = Output


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'products')
    list_display = ('name', 'products_count', 'outputs_count', 'norms_count')
    filter_horizontal = ('products',)
    inlines = (OutputInline, NormInline)
    actions = ['create_norms_dishes', 'create_outputs_dishes']

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

    def create_norms_dishes(self, request, queryset):
        groups = Group.objects.all()
        for dish in queryset:
            for group in groups.iterator():
                for product in dish.products.iterator():
                    for age_category in group.age_categories.iterator():
                        has_norm = dish.norms.filter(
                            product=product, group=group, age_category=age_category
                        ).exists()
                        if not has_norm:
                            norm = Norm.objects.create(
                                dish=dish,
                                product=product,
                                group=group,
                                age_category=age_category,
                                value=0.0,
                            )

    def create_outputs_dishes(self, request, queryset):
        groups = Group.objects.all()
        for dish in queryset:
            for group in groups.iterator():
                for age_category in group.age_categories.iterator():
                    has_output = dish.outputs.filter(
                        group=group, age_category=age_category
                    ).exists()
                    if not has_output:
                        output = Output.objects.create(
                            dish=dish, group=group, age_category=age_category, value='0'
                        )

    norms_count.short_description = _('Number of Products Norms')  # type: ignore
    outputs_count.short_description = _('Number of Products Outputs')  # type: ignore
    products_count.short_description = _('Number of Products')  # type: ignore
    create_norms_dishes.short_description = _(  # type: ignore
        'Creates norms for selected dishes'
    )
    create_outputs_dishes.short_description = _(  # type: ignore
        'Creates outputs for selected dishes'
    )
