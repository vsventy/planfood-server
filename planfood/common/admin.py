from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from planfood.products.models import Norm

from .models import AgeCategory, DishType, Group, ProductCategory


@admin.register(AgeCategory)
class AgeCategoryAdmin(admin.ModelAdmin):
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

    def products_count(self, obj):
        return obj.products.all().count()

    def norms_count(self, obj):
        return obj.product_norms.all().count()

    norms_count.short_description = _('Number of Products Norms')  # type: ignore
    products_count.short_description = _('Number of Products')  # type: ignore
