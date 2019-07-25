from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from planfood.products.models import Norm

from .models import AgeCategory, DefaultSettings, DishType, Group, ProductCategory


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultSettings)
class DefaultSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('sort', 'name', 'age_categories')
    filter_horizontal = ('age_categories',)


class NormInline(admin.TabularInline):
    model = Norm
    min_num = 2


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('sort', 'name')
    list_display = ('name', 'products_count', 'norms_count')
    inlines = (NormInline,)
    actions = ['create_norms_products']

    def products_count(self, obj):
        return obj.products.all().count()

    def norms_count(self, obj):
        return obj.product_norms.all().count()

    def create_norms_products(self, request, queryset):
        groups = Group.objects.all()
        for product_category in queryset:
            for group in groups.iterator():
                for age_category in group.age_categories.iterator():
                    has_norm = product_category.product_norms.filter(
                        group=group, age_category=age_category
                    ).exists()
                    if not has_norm:
                        norm = Norm.objects.create(
                            product_category=product_category,
                            group=group,
                            age_category=age_category,
                            value=0.0,
                        )

    norms_count.short_description = _('Number of Products Norms')  # type: ignore
    products_count.short_description = _('Number of Products')  # type: ignore
    create_norms_products.short_description = _(  # type: ignore
        'Creates norms for selected category of products'
    )
